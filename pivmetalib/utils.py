from __future__ import annotations

import logging
import pathlib
from typing import Dict, List, Union, Optional

import appdirs
import rdflib
import requests
from rdflib import Graph, Namespace, URIRef
from rdflib.util import guess_format

logger = logging.getLogger(__package__)
logger.setLevel('DEBUG')


class UNManager:
    """Manager class for URIRef and Namespace."""

    def __init__(self):
        self.data = {}

    def __getitem__(self, cls):
        if cls not in self.data:
            self.data[cls] = {}
        # there might be subclass to this cls. get those data as well
        for k, v in self.data.items():
            if k != cls:
                if issubclass(cls, k):
                    self.data[cls].update(v)
        return self.data[cls]


def split_URIRef(uri: rdflib.URIRef) -> List[Union[str, None]]:
    """Split a URIRef into namespace and key."""
    _uri = str(uri)
    if _uri.startswith('http'):
        if '#' in _uri:
            return _uri.rsplit('#', 1)
        _split = _uri.rsplit('/', 1)
        return [f'{_split[0]}/', _split[1]]
    if ':' in _uri:
        return _uri.rsplit(':', 1)
    return [None, uri]


# def merge_jsonld(jsonld_strings: List[str]) -> str:
#     """Merge multiple json-ld strings into one json-ld string."""
#     jsonld_dicts = [json.loads(jlds) for jlds in jsonld_strings]
#
#     contexts = []
#     for jlds in jsonld_dicts:
#         if jlds['@context'] not in contexts:
#             contexts.append(jlds['@context'])
#
#     out = {'@context': contexts,
#            '@graph': []}
#
#     for jlds in jsonld_dicts:
#         if '@graph' in jlds:
#             out['@graph'].append(jlds['@graph'])
#         else:
#             data = dict(jlds.items())
#             data.pop('@context')
#             out['@graph'].append(data)
#
#     return json.dumps(out, indent=2)


def get_cache_dir() -> pathlib.Path:
    """Get the cache directory and create it if it does not exist"""
    cache_dir = pathlib.Path(appdirs.user_cache_dir('pivmetalib'))
    if not cache_dir.exists():
        cache_dir.mkdir(parents=True)
    return cache_dir


def download_file(url,
                  dest_filename=None,
                  known_hash=None,
                  overwrite_existing: bool = False,
                  **kwargs) -> pathlib.Path:
    """Download a file from a URL and check its hash
    
    Parameter
    ---------
    url: str
        The URL of the file to download
    dest_filename: str or pathlib.Path =None
        The destination filename. If None, the filename is taken from the URL
    known_hash: str
        The expected hash of the file
    overwrite_existing: bool
        Whether to overwrite an existing file
    
    Returns
    -------
    pathlib.Path
        The path to the downloaded file

    Raises
    ------
    HTTPError if the request is not successful
    ValueError if the hash of the downloaded file does not match the expected hash
    """
    logger.debug(f'Performing request to {url}')
    response = requests.get(url, **kwargs)
    if not response.ok:
        response.raise_for_status()

    content = response.content

    # Calculate the hash of the downloaded content
    if known_hash:
        import hashlib
        calculated_hash = hashlib.sha256(content).hexdigest()
        if not calculated_hash == known_hash:
            raise ValueError('File does not match the expected has')

    total_size = int(response.headers.get("content-length", 0))
    block_size = 1024

    # Save the content to a file
    if dest_filename is None:
        filename = response.url.rsplit('/', 1)[1]
        dest_parent = get_cache_dir() / f'{total_size}'
        dest_filename = dest_parent / filename
        if dest_filename.exists():
            logger.debug(f'Taking existing file {dest_filename} and returning it.')
            return dest_filename
    else:
        dest_filename = pathlib.Path(dest_filename)
    dest_parent = dest_filename.parent
    if not dest_parent.exists():
        dest_parent.mkdir(parents=True)

    if dest_filename.exists():
        if overwrite_existing:
            logger.debug(f'Destination filename found: {dest_filename}. Deleting it, as overwrite_existing is True.')
            dest_filename.unlink()
        else:
            logger.debug(f'Destination filename found: {dest_filename}. Returning it')
            return dest_filename

    with open(dest_filename, "wb") as f:
        f.write(content)

    return dest_filename


PIV = Namespace("https://matthiasprobst.github.io/pivmeta#")
SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")
HDF5 = Namespace("http://purl.allotrope.org/ontologies/hdf5/1.8#")
XSD = Namespace("http://www.w3.org/2001/XMLSchema#")

SCHEME_QUERY = """
SELECT ?flag ?label ?meaning ?mask WHERE {
  VALUES ?scheme { <%(scheme)s> }
  ?scheme  <https://matthiasprobst.github.io/pivmeta#allowedFlag> ?flag .
  ?flag    <https://matthiasprobst.github.io/pivmeta#mask> ?mask .
  OPTIONAL { ?flag <http://www.w3.org/2004/02/skos/core#prefLabel> ?label . }
  OPTIONAL { ?flag <https://matthiasprobst.github.io/pivmeta#meaning> ?meaning . }
}
"""

ALL_FLAGS_QUERY = """
SELECT ?flag ?label ?meaning ?mask WHERE {
  ?flag a <https://matthiasprobst.github.io/pivmeta#Flag> ;
        <https://matthiasprobst.github.io/pivmeta#mask> ?mask .
  OPTIONAL { ?flag <http://www.w3.org/2004/02/skos/core#prefLabel> ?label . }
  OPTIONAL { ?flag <https://matthiasprobst.github.io/pivmeta#meaning> ?meaning . }
}
"""


def _ensure_graph(graph_or_path: Union[str, Graph]) -> Graph:
    if isinstance(graph_or_path, Graph):
        return graph_or_path
    g = Graph()
    g.bind("piv", PIV)
    g.bind("skos", SKOS)
    g.bind("hdf5", HDF5)
    g.bind("xsd", XSD)
    fmt = guess_format(graph_or_path)  # ttl, json-ld, xml, nt, etc.
    if fmt is None:
        if "@prefix" in graph_or_path:
            fmt = "ttl"
    g.parse(data=graph_or_path, format=fmt)
    return g


def _label_of(flag_uri: URIRef, label_lit, meaning_lit) -> str:
    # Prefer skos:prefLabel, then piv:meaning, then localname
    if label_lit:
        return str(label_lit)
    if meaning_lit:
        return str(meaning_lit)
    s = str(flag_uri)
    if "#" in s:
        return s.rsplit("#", 1)[1]
    if "/" in s:
        return s.rstrip("/").rsplit("/", 1)[-1]
    return s


def get_flag_table(
        graph_or_path: Union[str, Graph],
        scheme: Optional[str] = None
) -> List[Dict[str, Union[str, int]]]:
    """
    Returns a list of dicts: [{'uri': str, 'label': str, 'mask': int}, ...]
    If `scheme` is provided (IRI string), restricts to that scheme's piv:allowedFlag.
    """
    g = _ensure_graph(graph_or_path)
    q = SCHEME_QUERY % {"scheme": scheme} if scheme else ALL_FLAGS_QUERY

    rows = g.query(q)
    table: List[Dict[str, Union[str, int]]] = []
    seen = set()  # avoid duplicates

    for flag, label, meaning, mask in rows:
        key = (str(flag), int(mask.toPython()))
        if key in seen:
            continue
        seen.add(key)
        table.append({
            "uri": str(flag),
            "label": _label_of(flag, label, meaning),
            "mask": int(mask.toPython()),
        })
    # Stable sort by mask value
    table.sort(key=lambda r: r["mask"])
    return table


def get_flag_dict(
        graph_or_path: Union[str, Graph],
        scheme: Optional[str] = None
) -> Dict[str, int]:
    """
    Convenience: returns {label: mask}. If duplicate labels occur, last one wins.
    """
    return {row["label"]: row["mask"] for row in get_flag_table(graph_or_path, scheme)}
