from typing import Union

from ontolutils import namespaces, urirefs
from pydantic import HttpUrl, Field, field_validator

from pivmetalib import PIVMETA
from .. import m4i


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(WindowWeightingFunction='pivmeta:WindowWeightingFunction')
class WindowWeightingFunction(m4i.Method):
    """Implementation of pivmeta:CorrelationMethod"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(CorrelationMethod='pivmeta:CorrelationMethod',
         windowWeightingFunction='pivmeta:windowWeightingFunction')
class CorrelationMethod(m4i.Method):
    """Implementation of pivmeta:CorrelationMethod"""
    windowWeightingFunction: Union[HttpUrl, WindowWeightingFunction] = Field(alias='window_weighting_function')

    @field_validator('windowWeightingFunction', mode='before')
    @classmethod
    def _windowWeightingFunction(cls, window_weighting_function):
        if isinstance(window_weighting_function, str):
            if window_weighting_function.lower() in ('square', 'rectangle', 'none'):
                return str(PIVMETA.SquareWindowWeightingFunction)
            if window_weighting_function.lower() in ('gauss', 'gaussian'):
                return str(PIVMETA.GaussWindowWeightingFunction)
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
