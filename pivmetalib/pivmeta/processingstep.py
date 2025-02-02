from ontolutils import urirefs, namespaces

from pivmetalib import m4i


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVProcessingStep='pivmeta:PIVProcessingStep')
class PIVProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for pivmeta:PIVProcessingStep"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPostProcessing='pivmeta:PIVProcessingStep')
class PIVPostProcessing(PIVProcessingStep):
    """Pydantic Model for pivmeta:PIVPostProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPreProcessing='pivmeta:PIVPostProcessing')
class PIVPreProcessing(PIVProcessingStep):
    """Pydantic Model for pivmeta:PIVPreProcessing"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVEvaluation='pivmeta:PIVEvaluation')
class PIVEvaluation(PIVProcessingStep):
    """Pydantic Model for pivmeta:PIVEvaluation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVMaskGeneration='pivmeta:PIVMaskGeneration')
class PIVMaskGeneration(PIVProcessingStep):
    """Pydantic Model for pivmeta:MaskGeneration"""


# @namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
# @urirefs(ImageRotation='pivmeta:ImageRotation')
# class ImageRotation(PIVProcessingStep):
#     """Pydantic Model for pivmeta:ImageRotation"""


@namespaces(pivmeta='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVBackgroundGeneration='pivmeta:PIVBackgroundGeneration')
class PIVBackgroundGeneration(PIVProcessingStep):
    """Pydantic Model for pivmeta:BackgroundImageGeneration"""
