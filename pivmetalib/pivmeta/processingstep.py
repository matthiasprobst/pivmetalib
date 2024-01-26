from .. import m4i


class PivProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PivProcessingStep"""


class PivPostProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPostProcessing"""


class PivPreProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPreProcessing"""


class PivEvaluation(PivProcessingStep):
    """Pydantic Model for pivmeta:PivEvaluation"""


class MaskGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:MaskGeneration"""


class ImageRotation(PivProcessingStep):
    """Pydantic Model for pivmeta:ImageRotation"""


class BackgroundImageGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""

