from .. import m4i


class CorrelationAlgorithm(m4i.Method):
    """Implementation of pivmeta:CorrelationAlgorithm

    used by pivmeta:InterrogationMethod via property 'correlation algorithm'
    """


class InterrogationMethod(m4i.Method):
    """Implementation of pivmeta:InterrogationMethod"""
    correlation_algorithm: CorrelationAlgorithm


class Multigrid(InterrogationMethod):
    """Implementation of pivmeta:MultiGrid"""


class Multipass(InterrogationMethod):
    """Implementation of pivmeta:Multipass"""


class Singlepass(InterrogationMethod):
    """Implementation of pivmeta:Singlepass"""


setattr(InterrogationMethod, 'Multigrid', Multigrid)
setattr(InterrogationMethod, 'Multipass', Multipass)
setattr(InterrogationMethod, 'Singlepass', Singlepass)


class ImageManipulationMethod(m4i.Method):
    """Implementation of pivmeta:ImageManipulationMethod
    """
