from typing import Union, List

from ontolutils import namespaces, urirefs, Thing
from pydantic import PositiveInt, field_validator, Field, HttpUrl

from pivmetalib import PIVMETA
from pivmetalib.dcat import Distribution, Dataset
from pivmetalib.m4i import Variable


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(DataType='pivmeta:DataType')
class DataType(Thing):
    """Implementation of pivmeta:DataType"""
    pass


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVDistribution='pivmeta:PIVDistribution',
         hasDataType='pivmeta:hasDataType',
         hasMetric='pivmeta:hasMetric',
         filenamePattern='pivmeta:filenamePattern')
class PIVDistribution(Distribution):
    """Implementation of pivmeta:PIVDistribution

    Describes PIV data (images or result data)
    """
    hasDataType: Union[HttpUrl, str] = Field(default=None, alias='piv_distribution_type')
    filenamePattern: str = Field(default=None, alias='filename_pattern')  # e.g. "image_{:04d}.tif"
    hasMetric: Union[Variable, List[Variable]] = Field(default=None, alias='has_metric')

    @field_validator('filenamePattern', mode='before')
    @classmethod
    def _filenamePattern(cls, filenamePattern):
        return filenamePattern.replace('\\\\', '\\')

    @field_validator('hasDataType', mode='before')
    @classmethod
    def _isPIVDistributionType(cls, dist_type):
        return str(HttpUrl(dist_type))



# @namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVMaskDistribution='pivmeta:PIVMaskDistribution')
# class PIVMaskDistribution(PIVDistribution):
#     """Implementation of pivmeta:PIVMaskDistribution"""


# @namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
# @urirefs(PIVResultDistribution='pivmeta:PIVResultDistribution')
# class PIVResultDistribution(PIVDistribution):
#     """Implementation of pivmeta:PIVResultDistribution"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(PIVDataset='pivmeta:PIVDataset',
         distribution='dcat:distribution')
class PIVDataset(Dataset):
    """Implementation of pivmeta:PIVDataset"""""
    distribution: Union[Distribution, List[Distribution]] = Field(alias="distribution", default=None)
