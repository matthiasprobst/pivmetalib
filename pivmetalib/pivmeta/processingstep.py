from ontolutils import PIVMETA
from ontolutils import urirefs
from .. import m4i


@urirefs(PivProcessingStep=PIVMETA.PivProcessingStep)
class PivProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PivProcessingStep"""


@urirefs(PivPostProcessing=PIVMETA.PivProcessingStep)
class PivPostProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPostProcessing"""


@urirefs(PivPreProcessing=PIVMETA.PivPostProcessing)
class PivPreProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPreProcessing"""


@urirefs(PivEvaluation=PIVMETA.PIVEvaluation)
class PivEvaluation(PivProcessingStep):
    """Pydantic Model for pivmeta:PivEvaluation"""


@urirefs(MaskGeneration=PIVMETA.MaskGeneration)
class MaskGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:MaskGeneration"""


@urirefs(ImageRotation=PIVMETA.ImageRotation)
class ImageRotation(PivProcessingStep):
    """Pydantic Model for pivmeta:ImageRotation"""


@urirefs(BackgroundImageGeneration=PIVMETA.BackgroundImageGeneration)
class BackgroundImageGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""
