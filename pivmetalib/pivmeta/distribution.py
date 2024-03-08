import pathlib
import rdflib
import re
from enum import Enum
from ontolutils import namespaces, urirefs
from pydantic import HttpUrl, PositiveInt, field_validator
from typing import Union, List

from ..dcat import Distribution


class PivDistribution(Distribution):
    """Implementation of pivmeta:PivDistribution

    Describes PIV data (images or result data). See also subclasses PivImageDistribution and PivResultDistribution.
    """


class PivResultDistribution(Distribution):
    """Implementation of pivmeta:PivResultDistribution

    Describes PIV result data (e.g. csv or hdf files) which are experimental or synthetic data.
    """


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


class PivImageType(Enum):
    """Enumeration of possible PIV image types"""
    ExperimentalImage = "https://matthiasprobst.github.io/pivmeta#ExperimentalImage"
    SyntheticImage = "https://matthiasprobst.github.io/pivmeta#SyntheticImage"


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivDistribution='pivmeta:PivDistribution',
         filenamePattern='pivmeta:filenamePattern')
class PivDistribution(Distribution):
    """Implementation of pivmeta:PivDistribution

    Describes PIV data (images or result data). See also subclasses PivImageDistribution and PivResultDistribution.
    """
    filenamePattern: str = None  # e.g. "image_{:04d}.tif"

    @field_validator('filenamePattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')

    def get_filenames(self, file_directory: Union[str, pathlib.Path]) -> List[pathlib.Path]:
        """Returns a list of filenames in the given directory that match the filename pattern.

        Parameters
        ----------
        file_directory: Union[str, pathlib.Path]
            The path to the file directory. If not exists, first call .download()
            (or .download_and_unpack() if its a zipped file)

        Returns
        -------
        List[pathlib.Path]
            List of found filenames

        Raises
        ------
        ValueError:
            If parameter filenamePattern is unknown.
        """
        if self.filenamePattern is None:
            raise ValueError("The parameter filenamePattern is unknown")
        img_dir = pathlib.Path(file_directory)
        if isinstance(self.filenamePattern, str):
            pattern = re.compile(self.filenamePattern)
        filenames = []
        for f in img_dir.iterdir():
            if f.is_file():
                if pattern.match(f.name):
                    filenames.append(f)
        return filenames


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivImageDistribution='pivmeta:PivImageDistribution',
         pivImageType='pivmeta:pivImageType',
         imageBitDepth='pivmeta:imageBitDepth',
         numberOfRecords='pivmeta:numberOfRecords')
class PivImageDistribution(PivDistribution):
    """Implementation of pivmeta:PivImageDistribution

    Describes PIV images (e.g. tiff files) which are experimental or synthetic data.
    """
    pivImageType: Union[HttpUrl, PivImageType] = None
    imageBitDepth: PositiveInt = None
    numberOfRecords: PositiveInt = None

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        if str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#ExperimentalImage":
            pit = make_href("https://matthiasprobst.github.io/pivmeta#ExperimentalImage", "experimental")
            return f"{self.__class__.__name__}('{pit}', {make_href(self.downloadURL)})"
        elif str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#SyntheticImage":
            pit = make_href("https://matthiasprobst.github.io/pivmeta#SyntheticImage", "synthetic")
            return f"{self.__class__.__name__}('{pit}', {make_href(self.downloadURL)})"
        return f"{self.__class__.__name__}({make_href(self.downloadURL)})"

    @field_validator('pivImageType', mode='before')
    @classmethod
    def _pivImageType(cls, pivImageType):
        if isinstance(pivImageType, rdflib.URIRef):
            return str(pivImageType)
        if isinstance(pivImageType, PivImageType):
            return pivImageType.value
        return pivImageType

    def is_synthetic(self) -> bool:
        """Returns True if the PIV image is synthetic, False otherwise."""
        return self.pivImageType == PivImageType.SyntheticImage.value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivMaskDistribution='pivmeta:PivMaskDistribution')
class PivMaskDistribution(PivDistribution):
    """Implementation of pivmeta:PivMaskDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivResultDistribution='pivmeta:PivResultDistribution')
class PivResultDistribution(PivDistribution):
    """Implementation of pivmeta:PivResultDistribution"""
