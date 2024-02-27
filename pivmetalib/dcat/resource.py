"""Implementation of classes
- dcat:Resource
- dcat:Distribution
- dcat:Dataset
"""
import pathlib
import re
import shutil
import uuid
from datetime import datetime
from dateutil import parser
from pydantic import HttpUrl, FileUrl, field_validator
from typing import Union, List

from ..owl import Thing
from ..prov import Person, Organisation, Agent
from ..model import namespaces, context
from ..utils import download_file
from ..utils import is_zip_file, get_cache_dir


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
         downloadURL='dcat:downloadURL',
         mediaType='dcat:mediaType',
         byteSize='dcat:byteSize',
         keyword='dcat:keyword')
class Distribution(Resource):
    """Implementation of dcat:Distribution

    .. note::
        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    downloadURL: Union[HttpUrl, FileUrl]
        Download URL of the distribution (dcat:downloadURL)
    mediaType: HttpUrl = None
        Media type of the distribution (dcat:mediaType).
        Should be defined by the [IANA Media Types registry](https://www.iana.org/assignments/media-types/media-types.xhtml)
    byteSize: int = None
        Size of the distribution in bytes (dcat:byteSize)
    """
    downloadURL: Union[HttpUrl, FileUrl] = None  # dcat:downloadURL, e.g.
    mediaType: HttpUrl = None  # dcat:mediaType
    byteSize: int = None  # dcat:byteSize
    keyword: List[str] = None  # dcat:keyword

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        if self.downloadURL is not None:
            return f"{self.__class__.__name__}({self.downloadURL})"
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
            fname = pathlib.Path(self.downloadURL.path[1:])
            if fname.exists():
                return fname
            raise FileNotFoundError(f'File {self.downloadURL.path} does not exist')

        if self.downloadURL.scheme == 'file':
            if dest_filename is None:
                return _parse_file_url(self.downloadURL.path)
            else:
                return shutil.copy(_parse_file_url(self.downloadURL.path), dest_filename)
        dest_filename = pathlib.Path(dest_filename or self.downloadURL.path.split('/')[-1])
        if dest_filename.exists():
            return dest_filename
        return download_file(self.downloadURL,
                             dest_filename,
                             overwrite_existing=overwrite_existing)

    def download_and_unpack(
            self,
            target_dir: Union[str, pathlib.Path]) -> pathlib.Path:
        """Download the data and unpack it. This makes sense if the file
        source is a zip file"""
        if not is_zip_file(self.mediaType):
            raise ValueError('The distribution does not seem to be a ZIP file. '
                             f'The media type is {self.mediaType} but '
                             '"https://www.iana.org/assignments/media-types/application/zip" '
                             'is expected')
        import zipfile
        zip_filename = self.download(
            dest_filename=get_cache_dir() / f'{uuid.uuid4()}.zip'
        )
        with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        return target_dir

    @field_validator('mediaType', mode='before')
    @classmethod
    def _mediaType(cls, mediaType):
        """should be a valid URI, like: https://www.iana.org/assignments/media-types/text/markdown"""
        if isinstance(mediaType, str):
            if mediaType.startswith('http'):
                return HttpUrl(mediaType)
            elif mediaType.startswith('iana:'):
                return HttpUrl("https://www.iana.org/assignments/media-types/" + mediaType.split(":", 1)[-1])
            elif re.match('[a-z].*/[a-z].*', mediaType):
                return HttpUrl("https://www.iana.org/assignments/media-types/" + mediaType)
        return mediaType


@namespaces(dcat="http://www.w3.org/ns/dcat#",
            prov="http://www.w3.org/ns/prov#",
            dct="http://purl.org/dc/terms/")
@context(Dataset='dcat:Dataset',
         identifier='dct:identifier',
         creator='dct:creator',
         distribution='dcat:distribution',
         modified='dct:modified',
         landingPage='dcat:landingPage')
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
