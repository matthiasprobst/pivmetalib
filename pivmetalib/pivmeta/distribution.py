from typing import Union, Any

from ontolutils import namespaces, urirefs
from pydantic import HttpUrl, PositiveInt, field_validator, Field

from pivmetalib import PIVMETA
from pivmetalib.dcat import Distribution


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVDistribution='pivmeta:PIVDistribution',
         filenamePattern='pivmeta:filenamePattern')
class PIVDistribution(Distribution):
    """Implementation of pivmeta:PIVDistribution

    Describes PIV data (images or result data). See also subclasses PIVImageDistribution and PIVResultDistribution.
    """
    filenamePattern: str = Field(default=None, alias='filename_pattern')  # e.g. "image_{:04d}.tif"

    @field_validator('filenamePattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVImageDistribution='pivmeta:PIVImageDistribution',
         pivImageType='pivmeta:pivImageType',
         imageBitDepth='pivmeta:imageBitDepth',
         numberOfRecords='pivmeta:numberOfRecords')
class PIVImageDistribution(PIVDistribution):
    """Implementation of pivmeta:PIVImageDistribution

    Describes PIV images (e.g. tiff files) which are experimental or synthetic data.
    """
    pivImageType: Union[HttpUrl, str] = Field(default=None, alias="piv_image_type")
    imageBitDepth: PositiveInt = Field(default=None, alias="image_bit_depth")
    numberOfRecords: PositiveInt = Field(default=None, alias="number_of_records")

    # def _repr_html_(self):
    #     """Returns the HTML representation of the class"""
    #     if str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#ExperimentalImage":
    #         pit = make_href("https://matthiasprobst.github.io/pivmeta#ExperimentalImage", "experimental")
    #         return f"{self.__class__.__name__}('{pit}', {make_href(selfdownload_URL)})"
    #     elif str(self.pivImageType) == "https://matthiasprobst.github.io/pivmeta#SyntheticImage":
    #         pit = make_href("https://matthiasprobst.github.io/pivmeta#SyntheticImage", "synthetic")
    #         return f"{self.__class__.__name__}('{pit}', {make_href(selfdownload_URL)})"
    #     return f"{self.__class__.__name__}({make_href(selfdownload_URL)})"

    @field_validator('pivImageType', mode='before')
    @classmethod
    def _pivImageType(cls, piv_image_type):
        return str(HttpUrl(piv_image_type))

    def is_synthetic(self) -> bool:
        """Returns True if the PIV image is synthetic, False otherwise."""
        return self.piv_image_type == PIVMETA.SyntheticImage


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVMaskDistribution='pivmeta:PIVMaskDistribution')
class PIVMaskDistribution(PIVDistribution):
    """Implementation of pivmeta:PIVMaskDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVResultDistribution='pivmeta:PIVResultDistribution')
class PIVResultDistribution(PIVDistribution):
    """Implementation of pivmeta:PIVResultDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(PIVDataset='pivmeta:PIVDataset',
         distribution='dcat:distribution')
class PIVDataset(PIVDistribution):
    """Implementation of pivmeta:PIVDataset"""""
    distribution: Any = Field(alias="distribution", default=None)  # TODO: fix!
