from .. import m4i


class PivProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PivProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """


class MaskGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:MaskGeneration"""


class ImageManipulation(PivProcessingStep):
    """Pydantic Model for pivmeta:ImageManipulation"""


class BackgroundImageGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""


class PostProcessingStep(PivProcessingStep):
    """Pydantic Model for pivmeta:PostProcessingStep"""
