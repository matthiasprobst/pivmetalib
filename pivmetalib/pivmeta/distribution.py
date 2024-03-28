from enum import Enum
from typing import Union

import rdflib
from pydantic import HttpUrl, PositiveInt, field_validator, Field

from ontolutils import namespaces, urirefs
from ontolutils.namespacelib import PIVMETA
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
    ExperimentalImage = PIVMETA.ExperimentalImage  # https://matthiasprobst.github.io/pivmeta#ExperimentalImage
    SyntheticImage = PIVMETA.SyntheticImage  # https://matthiasprobst.github.io/pivmeta#SyntheticImage


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivDistribution='pivmeta:PivDistribution',
         filename_pattern='pivmeta:filenamePattern')
class PivDistribution(Distribution):
    """Implementation of pivmeta:PivDistribution

    Describes PIV data (images or result data). See also subclasses PivImageDistribution and PivResultDistribution.
    """
    filename_pattern: str = Field(default=None, alias='filenamePattern')  # e.g. "image_{:04d}.tif"

    @field_validator('filename_pattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivImageDistribution='pivmeta:PivImageDistribution',
         piv_image_type='pivmeta:pivImageType',
         image_bit_depth='pivmeta:imageBitDepth',
         number_of_records='pivmeta:numberOfRecords')
class PivImageDistribution(PivDistribution):
    """Implementation of pivmeta:PivImageDistribution

    Describes PIV images (e.g. tiff files) which are experimental or synthetic data.
    """
    piv_image_type: Union[HttpUrl, PivImageType] = Field(default=None, alias="pivImageType")
    image_bit_depth: PositiveInt = Field(default=None, alias="imageBitDepth")
    number_of_records: PositiveInt = Field(default=None, alias="numberOfRecords")

    # def _repr_html_(self):
    #     """Returns the HTML representation of the class"""
    #     if str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#ExperimentalImage":
    #         pit = make_href("https://matthiasprobst.github.io/pivmeta#ExperimentalImage", "experimental")
    #         return f"{self.__class__.__name__}('{pit}', {make_href(selfdownload_URL)})"
    #     elif str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#SyntheticImage":
    #         pit = make_href("https://matthiasprobst.github.io/pivmeta#SyntheticImage", "synthetic")
    #         return f"{self.__class__.__name__}('{pit}', {make_href(selfdownload_URL)})"
    #     return f"{self.__class__.__name__}({make_href(selfdownload_URL)})"

    @field_validator('piv_image_type', mode='before')
    @classmethod
    def _pivImageType(cls, piv_image_type):
        if isinstance(piv_image_type, rdflib.URIRef):
            return str(piv_image_type)
        if isinstance(piv_image_type, PivImageType):
            return piv_image_type.value
        return piv_image_type

    def is_synthetic(self) -> bool:
        """Returns True if the PIV image is synthetic, False otherwise."""
        return self.piv_image_type == PivImageType.SyntheticImage.value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivMaskDistribution='pivmeta:PivMaskDistribution')
class PivMaskDistribution(PivDistribution):
    """Implementation of pivmeta:PivMaskDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivResultDistribution='pivmeta:PivResultDistribution')
class PivResultDistribution(PivDistribution):
    """Implementation of pivmeta:PivResultDistribution"""
