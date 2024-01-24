"""Implementation of classes
- dcat:Resource
- dcat:Distribution
- dcat:Dataset
"""
import pathlib
import re
import shutil
from datetime import datetime
from dateutil import parser
from pydantic import HttpUrl, FileUrl, field_validator
from typing import Union, List

from ..core import Thing
from ..prov import Person, Organization
from ..utils import download_file


class Resource(Thing):
    """Pyantic implementation of dcat:Resource

    .. note::

        More than the below parameters are possible but not explicitly defined here.



    Parameters
    ----------
    title: str
        Title of the resource (dcterms:title)
    description: str = None
        Description of the resource (dcterms:description)
    creator: Union[Person, Organization] = None
        Creator of the resource (dcterms:creator)
    version: str = None
        Version of the resource (dcat:version)
    """
    title: str  # dcterms:title
    description: str = None  # dcterms:description
    creator: Union[Person, Organization] = None  # dcterms:creator
    version: str = None  # dcat:version

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.title})"


class Distribution(Resource):
    """Implementation of dcat:Distribution

    .. note::
        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    download_URL: Union[HttpUrl, FileUrl]
        Download URL of the distribution (dcat:download_URL)
    media_type: HttpUrl = None
        Media type of the distribution (dcat:media_type).
        Should be defined by the [IANA Media Types registry](https://www.iana.org/assignments/media-types/media-types.xhtml)
    byte_size: int = None
        Size of the distribution in bytes (dcat:byte_size)
    """
    download_URL: Union[HttpUrl, FileUrl]  # dcat:download_URL, e.g.
    media_type: HttpUrl = None  # dcat:media_type
    byte_size: int = None  # dcat:byte_size
    keyword: List[str] = None  # dcat:keyword

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.download_URL})"

    def download(self,
                 dest_filename: Union[str, pathlib.Path] = None,
                 overwrite_existing: bool = False) -> pathlib.Path:
        """Downloads the distribution"""

        def _parse_file_url(furl):
            """in windows, we might need to strip the leading slash"""
            fname = pathlib.Path(furl)
            if fname.exists():
                return fname
            fname = pathlib.Path(self.download_URL.path[1:])
            if fname.exists():
                return fname
            raise FileNotFoundError(f'File {self.download_URL.path} does not exist')

        if self.download_URL.scheme == 'file':
            if dest_filename is None:
                return _parse_file_url(self.download_URL.path)
            else:
                return shutil.copy(_parse_file_url(self.download_URL.path), dest_filename)
        return download_file(self.download_URL,
                             dest_filename,
                             overwrite_existing=overwrite_existing)

    @field_validator('media_type', mode='before')
    @classmethod
    def _mediaType(cls, media_type):
        """should be a valid URI, like: https://www.iana.org/assignments/media-types/text/markdown"""
        if isinstance(media_type, str):
            if media_type.startswith('http'):
                return HttpUrl(media_type)
            elif media_type.startswith('iana:'):
                return HttpUrl("https://www.iana.org/assignments/media-types/" + media_type.split(":", 1)[-1])
            elif re.match('[a-z].*/[a-z].*', media_type):
                return HttpUrl("https://www.iana.org/assignments/media-types/" + media_type)
        return media_type


class Dataset(Resource):
    """Pydantic implementation of dcat:Dataset

    .. note::

        More than the below parameters are possible but not explicitly defined here.



    Parameters
    ----------
    title: str
        Title of the resource (dcterms:title)
    description: str = None
        Description of the resource (dcterms:description)
    creator: Union[Person, Organization] = None
        Creator of the resource (dcterms:creator)
    version: str = None
        Version of the resource (dcat:version)
    identifier: HttpUrl = None
        Identifier of the resource (dcterms:identifier)
    contact: Union[Person, Organization] = None
        Contact person or organization of the resource (http://www.w3.org/ns/prov#Person)
    distribution: List[Distribution] = None
        Distribution of the resource (dcat:Distribution)
    modified: datetime = None
        Last modified date of the resource (dcterms:modified)
    """
    identifier: HttpUrl = None  # dcterms:identifier, see https://www.w3.org/TR/vocab-dcat-3/#ex-identifier
    # http://www.w3.org/ns/prov#Person, see https://www.w3.org/TR/vocab-dcat-3/#ex-adms-identifier
    contact: Union[Person, Organization] = None
    distribution: Union[Distribution, List[Distribution]] = None  # dcat:Distribution
    modified: datetime = None  # dcterms:modified
    landingPage: HttpUrl = None  # dcat:landingPage

    @field_validator('modified', mode='before')
    @classmethod
    def _modified(cls, modified):
        """parse datetime"""
        if isinstance(modified, str):
            return parser.parse(modified)
        return modified
