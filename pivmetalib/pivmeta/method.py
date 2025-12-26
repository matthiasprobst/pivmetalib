from typing import Union

from ontolutils import namespaces, urirefs
from ontolutils.ex import m4i
from pydantic import HttpUrl, Field, field_validator

from pivmetalib import PIV


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(WindowWeightingFunction='piv:WindowWeightingFunction')
class WindowWeightingFunction(m4i.Method):
    """Implementation of piv:CorrelationMethod"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(CorrelationMethod='piv:CorrelationMethod',
         hasWindowWeightingFunction='piv:hasWindowWeightingFunction')
class CorrelationMethod(m4i.Method):
    """Implementation of piv:CorrelationMethod"""
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


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(InterrogationMethod='piv:InterrogationMethod')
class InterrogationMethod(m4i.Method):
    """Implementation of piv:InterrogationMethod"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ImageManipulationMethod='piv:ImageManipulationMethod')
class ImageManipulationMethod(m4i.Method):
    """Implementation of piv:ImageManipulationMethod"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OutlierDetectionMethod='piv:OutlierDetectionMethod')
class OutlierDetectionMethod(m4i.Method):
    """Implementation of piv:OutlierDetectionMethod"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Multigrid='piv:Multigrid')
class Multigrid(InterrogationMethod):
    """Implementation of piv:MultiGrid"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Multipass='piv:Multipass')
class Multipass(InterrogationMethod):
    """Implementation of piv:Multipass"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Singlepass='piv:Singlepass')
class Singlepass(InterrogationMethod):
    """Implementation of piv:Singlepass"""
