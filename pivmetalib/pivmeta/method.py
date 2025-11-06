from typing import Union

from ontolutils import namespaces, urirefs
from pydantic import HttpUrl, Field, field_validator

from ontolutils.ex import m4i
from pivmetalib import PIV


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(WindowWeightingFunction='pivmeta:WindowWeightingFunction')
class WindowWeightingFunction(m4i.Method):
    """Implementation of pivmeta:CorrelationMethod"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(CorrelationMethod='pivmeta:CorrelationMethod',
         hasWindowWeightingFunction='pivmeta:hasWindowWeightingFunction')
class CorrelationMethod(m4i.Method):
    """Implementation of pivmeta:CorrelationMethod"""
    hasWindowWeightingFunction: Union[HttpUrl, WindowWeightingFunction] = Field(alias='has_window_weighting_function')

    @field_validator('hasWindowWeightingFunction', mode='before')
    @classmethod
    def _hasWindowWeightingFunction(cls, window_weighting_function):
        if isinstance(window_weighting_function, str):
            if window_weighting_function.lower() in ('square', 'rectangle', 'none'):
                return str(PIV.SquareWindow)
            if window_weighting_function.lower() in ('gauss', 'gaussian'):
                return str(PIV.GaussianWindow)
        return window_weighting_function


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(InterrogationMethod='pivmeta:InterrogationMethod')
class InterrogationMethod(m4i.Method):
    """Implementation of pivmeta:InterrogationMethod"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ImageManipulationMethod='pivmeta:ImageManipulationMethod')
class ImageManipulationMethod(m4i.Method):
    """Implementation of pivmeta:ImageManipulationMethod"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OutlierDetectionMethod='pivmeta:OutlierDetectionMethod')
class OutlierDetectionMethod(m4i.Method):
    """Implementation of pivmeta:OutlierDetectionMethod"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Multigrid='pivmeta:Multigrid')
class Multigrid(InterrogationMethod):
    """Implementation of pivmeta:MultiGrid"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Multipass='pivmeta:Multipass')
class Multipass(InterrogationMethod):
    """Implementation of pivmeta:Multipass"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Singlepass='pivmeta:Singlepass')
class Singlepass(InterrogationMethod):
    """Implementation of pivmeta:Singlepass"""
