from typing import Union, List, Optional

from ontolutils import namespaces, urirefs, Thing
from ontolutils.ex.dcat import Distribution, Dataset
from ontolutils.typing import ResourceType
from pydantic import field_validator, Field, HttpUrl
from ssnolib.m4i import NumericalVariable
from ssnolib.pimsii import Variable


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVDataType='piv:PIVDataType')
class PIVDataType(Thing):
    """Implementation of piv:PIVDataType"""
    pass


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ImageVelocimetryDistribution='piv:ImageVelocimetryDistribution',
         hasPIVDataType='piv:hasPIVDataType',
         hasMetric='piv:hasMetric',
         filenamePattern='piv:filenamePattern')
class ImageVelocimetryDistribution(Distribution):
    """Implementation of piv:ImageVelocimetryDistribution

    Describes PIV data (images or result data)
    """
    hasPIVDataType: Optional[Union[ResourceType, str]] = Field(default=None, alias='has_piv_data_type')
    filenamePattern: Optional[str] = Field(default=None, alias='filename_pattern')  # e.g. "image_{:04d}.tif"
    hasMetric: Optional[Union[Variable, NumericalVariable, List[Union[Variable, NumericalVariable]]]] = Field(
        default=None,
                                                                                                    alias='has_metric')

    @field_validator('filenamePattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')

    @field_validator('hasPIVDataType', mode='before')
    @classmethod
    def _hasPIVDataType(cls, dist_type):
        return str(HttpUrl(dist_type))


# @namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVMaskDistribution='piv:PIVMaskDistribution')
# class PIVMaskDistribution(ImageVelocimetryDistribution):
#     """Implementation of piv:PIVMaskDistribution"""


# @namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVResultDistribution='piv:PIVResultDistribution')
# class PIVResultDistribution(ImageVelocimetryDistribution):
#     """Implementation of piv:PIVResultDistribution"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(ImageVelocimetryDataset='piv:ImageVelocimetryDataset',
         distribution='dcat:distribution')
class ImageVelocimetryDataset(Dataset):
    """Implementation of piv:ImageVelocimetryDataset"""""
    distribution: Union[Distribution, List[Distribution]] = Field(alias="distribution", default=None)
