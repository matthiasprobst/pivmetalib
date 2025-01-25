from ontolutils import urirefs, namespaces

from pivmetalib import m4i


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVAnalysis='pivmeta:PIVAnalysis')
class PIVAnalysis(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PIVAnalysis"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPostProcessing='pivmeta:PIVAnalysis')
class PIVPostProcessing(PIVAnalysis):
    """Pydantic Model for pivmeta:PIVPostProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPreProcessing='pivmeta:PIVPostProcessing')
class PIVPreProcessing(PIVAnalysis):
    """Pydantic Model for pivmeta:PIVPreProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVEvaluation='pivmeta:PIVEvaluation')
class PIVEvaluation(PIVAnalysis):
    """Pydantic Model for pivmeta:PIVEvaluation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(MaskGeneration='pivmeta:MaskGeneration')
class MaskGeneration(PIVAnalysis):
    """Pydantic Model for pivmeta:MaskGeneration"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(ImageRotation='pivmeta:ImageRotation')
class ImageRotation(PIVAnalysis):
    """Pydantic Model for pivmeta:ImageRotation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(BackgroundImageGeneration='pivmeta:BackgroundImageGeneration')
class BackgroundImageGeneration(PIVAnalysis):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""
