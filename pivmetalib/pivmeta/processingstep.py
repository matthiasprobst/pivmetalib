from ontolutils import urirefs, namespaces
from .. import m4i


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PivProcessingStep='pivmeta:PivProcessingStep')
class PivProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PivProcessingStep"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PivPostProcessing='pivmeta:PivProcessingStep')
class PivPostProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPostProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PivPreProcessing='pivmeta:PivPostProcessing')
class PivPreProcessing(PivProcessingStep):
    """Pydantic Model for pivmeta:PivPreProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PivEvaluation='pivmeta:PIVEvaluation')
class PivEvaluation(PivProcessingStep):
    """Pydantic Model for pivmeta:PivEvaluation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(MaskGeneration='pivmeta:MaskGeneration')
class MaskGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:MaskGeneration"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(ImageRotation='pivmeta:ImageRotation')
class ImageRotation(PivProcessingStep):
    """Pydantic Model for pivmeta:ImageRotation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(BackgroundImageGeneration='pivmeta:BackgroundImageGeneration')
class BackgroundImageGeneration(PivProcessingStep):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""
