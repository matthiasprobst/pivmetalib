from ontolutils import namespaces, urirefs

from .. import m4i


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(CorrelationAlgorithm='pivmeta:CorrelationAlgorithm')
class CorrelationAlgorithm(m4i.Method):
    """Implementation of pivmeta:CorrelationAlgorithm

    used by pivmeta:InterrogationMethod via property 'correlation algorithm'
    """


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(InterrogationMethod='pivmeta:CrossCorrelation')
class InterrogationMethod(m4i.Method):
    """Implementation of pivmeta:InterrogationMethod"""


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


setattr(InterrogationMethod, 'Multigrid', Multigrid)
setattr(InterrogationMethod, 'Multipass', Multipass)
setattr(InterrogationMethod, 'Singlepass', Singlepass)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ImageManipulationMethod='pivmeta:ImageManipulationMethod')
class ImageManipulationMethod(m4i.Method):
    """Implementation of pivmeta:ImageManipulationMethod
    """


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OutlierDetectionMethod='pivmeta:OutlierDetectionMethod')
class OutlierDetectionMethod(m4i.Method):
    """Implementation of pivmeta:OutlierDetectionMethod"""
