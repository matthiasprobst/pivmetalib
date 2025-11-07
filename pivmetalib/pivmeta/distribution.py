from typing import Union, List

from ontolutils import namespaces, urirefs, Thing
from ontolutils.ex.dcat import Distribution, Dataset
from pydantic import field_validator, Field, HttpUrl
from ssnolib.m4i import NumericalVariable
from ssnolib.pimsii import Variable


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVDataType='pivmeta:PIVDataType')
class PIVDataType(Thing):
    """Implementation of pivmeta:PIVDataType"""
    pass


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ImageVelocimetryDistribution='pivmeta:ImageVelocimetryDistribution',
         hasPIVDataType='pivmeta:hasPIVDataType',
         hasMetric='pivmeta:hasMetric',
         filenamePattern='pivmeta:filenamePattern')
class ImageVelocimetryDistribution(Distribution):
    """Implementation of pivmeta:ImageVelocimetryDistribution

    Describes PIV data (images or result data)
    """
    hasPIVDataType: Union[HttpUrl, str] = Field(default=None, alias='has_piv_data_type')
    filenamePattern: str = Field(default=None, alias='filename_pattern')  # e.g. "image_{:04d}.tif"
    hasMetric: Union[Variable, NumericalVariable, List[Union[Variable, NumericalVariable]]] = Field(default=None,
                                                                                                    alias='has_metric')

    @field_validator('filenamePattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')

    @field_validator('hasPIVDataType', mode='before')
    @classmethod
    def _hasPIVDataType(cls, dist_type):
        return str(HttpUrl(dist_type))


# @namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVMaskDistribution='pivmeta:PIVMaskDistribution')
# class PIVMaskDistribution(ImageVelocimetryDistribution):
#     """Implementation of pivmeta:PIVMaskDistribution"""


# @namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVResultDistribution='pivmeta:PIVResultDistribution')
# class PIVResultDistribution(ImageVelocimetryDistribution):
#     """Implementation of pivmeta:PIVResultDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(ImageVelocimetryDataset='pivmeta:ImageVelocimetryDataset',
         distribution='dcat:distribution')
class ImageVelocimetryDataset(Dataset):
    """Implementation of pivmeta:ImageVelocimetryDataset"""""
    distribution: Union[Distribution, List[Distribution]] = Field(alias="distribution", default=None)
