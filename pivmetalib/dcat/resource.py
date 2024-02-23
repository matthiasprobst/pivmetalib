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

from ..owl import Thing
from ..prov import Person, Organisation, Agent
from ..template import namespaces, context
from ..utils import download_file


@namespaces(dcat="http://www.w3.org/ns/dcat#",
            dct="http://purl.org/dc/terms/", )
@context(Resource='dcat:Resource',
         title='dct:title',
         description='dct:description',
         creator='dct:creator',
         version='dcat:version')
class Resource(Thing):
    """Pdyantic implementation of dcat:Resource

    .. note::

        More than the below parameters are possible but not explicitly defined here.



    Parameters
    ----------
    title: str
        Title of the resource (dct:title)
    description: str = None
        Description of the resource (dct:description)
    creator: Union[Person, Organisation] = None
        Creator of the resource (dct:creator)
    version: str = None
        Version of the resource (dcat:version)
    """
    title: str = None  # dct:title
    description: str = None  # dct:description
    creator: Union[Person, Organisation] = None  # dct:creator
    version: str = None  # dcat:version


    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.title})"


@namespaces(dcat="http://www.w3.org/ns/dcat#")
@context(Distribution='dcat:Distribution',
         download_URL='dcat:downloadURL',
         media_type='dcat:mediaType',
         byte_size='dcat:byteSize',
         keyword='dcat:keyword')
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
    download_URL: Union[HttpUrl, FileUrl] = None  # dcat:downloadURL, e.g.
    media_type: HttpUrl = None  # dcat:mediaType
    byte_size: int = None  # dcat:byte_size
    keyword: List[str] = None  # dcat:keyword

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        if self.download_URL is not None:
            return f"{self.__class__.__name__}({self.download_URL})"
        return super()._repr_html_()

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


@namespaces(dcat="http://www.w3.org/ns/dcat#",
            prov="http://www.w3.org/ns/prov#",
            dct="http://purl.org/dc/terms/")
@context(Dataset='dcat:Dataset',
         identifier='dct:identifier',
         creator='dct:creator',
         distribution='dcat:distribution',
         modified='dct:modified')
class Dataset(Resource):
    """Pydantic implementation of dcat:Dataset

    .. note::

        More than the below parameters are possible but not explicitly defined here.



    Parameters
    ----------
    title: str
        Title of the resource (dct:title)
    description: str = None
        Description of the resource (dct:description)
    creator: Agent = None
        Creator of the resource (dct:creator)
    version: str = None
        Version of the resource (dcat:version)
    identifier: HttpUrl = None
        Identifier of the resource (dct:identifier)
    creator: Union[Person, Organisation] = None  # dct:creator
        Contact person or Organisation of the resource (http://www.w3.org/ns/prov#Person)
    distribution: List[Distribution] = None
        Distribution of the resource (dcat:Distribution)
    modified: datetime = None
        Last modified date of the resource (dct:modified)
    """
    identifier: HttpUrl = None  # dct:identifier, see https://www.w3.org/TR/vocab-dcat-3/#ex-identifier
    # http://www.w3.org/ns/prov#Person, see https://www.w3.org/TR/vocab-dcat-3/#ex-adms-identifier
    creator: Agent = None
    distribution: Union[Distribution, List[Distribution]] = None  # dcat:Distribution
    modified: datetime = None  # dct:modified
    landingPage: HttpUrl = None  # dcat:landingPage

    @field_validator('distribution', mode='before')
    @classmethod
    def _distribution(cls, distribution):
        if not isinstance(distribution, list):
            return [distribution]
        return distribution
        # def _parse_dist(_dist):
        #     if isinstance(_dist, str):
        #         return Distribution(id=_dist)
        #     return _dist
        #
        # if isinstance(distribution, list):
        #     return [_parse_dist(_dist) for _dist in distribution]
        # return _parse_dist(distribution)

    @field_validator('modified', mode='before')
    @classmethod
    def _modified(cls, modified):
        """parse datetime"""
        if isinstance(modified, str):
            return parser.parse(modified)
        return modified
