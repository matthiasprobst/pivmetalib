import logging
import requests
from typing import Dict

from . import utils
from ._version import __version__
from .decorator import namespaces, urirefs
from .model import PivMetaBaseModel
from .namespace import PIVMETA
from .owl import Thing
from .query_util import query

DEFAULT_LOGGING_LEVEL = logging.WARNING
_formatter = logging.Formatter(
    '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d_%H:%M:%S')

_stream_handler = logging.StreamHandler()
_stream_handler.setLevel(DEFAULT_LOGGING_LEVEL)
_stream_handler.setFormatter(_formatter)

logger = logging.getLogger(__package__)
logger.addHandler(_stream_handler)

CONTEXT = "https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld"
CACHE_DIR = utils.get_cache_dir()


def get_context_json() -> Dict:
    """Get the context file as a json object."""
    r = requests.get(CONTEXT)
    r.raise_for_status()
    return r.json()


def get_iri_fields(obj: PivMetaBaseModel):
    """Get field names and their corresponding IRIs from the context file.

    Example:
    --------
    @namespaces(name="http://example.com/name", age="http://example.com/age")
    class ExampleModel(PivMetaBaseModel):
        name: str
        age: int

    em = ExampleModel(name="test", age=10)
    print(pivmetalib.get_iri_fields(em))
    # {'name': 'http://example.com/name', 'age': 'http://example.com/age'}
    """
    from .decorator import URIRefManager, NamespaceManager
    namespaces = NamespaceManager[obj.__class__]
    iri_fields = {}
    for k, v in URIRefManager[obj.__class__].items():
        ns, key = utils.split_URIRef(v)
        full_ns = namespaces.get(ns, None)
        if full_ns is None:
            iri_fields[k] = v
        else:
            iri_fields[k] = f'{full_ns}{key}'
    return iri_fields


__all__ = (
    '__version__',
    'Thing',
    'CONTEXT',
    'CACHE_DIR',
    'get_context_json',
    'PIVMETA',
    'namespaces',
    'urirefs'
)
