from ontolutils import urirefs, namespaces
from ontolutils.ex import m4i


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVProcessingStep='piv:PIVProcessingStep')
class PIVProcessingStep(m4i.ProcessingStep):
    """Pydantic Model for piv:PIVProcessingStep"""


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPostProcessing='piv:PIVProcessingStep')
class PIVPostProcessing(PIVProcessingStep):
    """Pydantic Model for piv:PIVPostProcessing"""


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVPreProcessing='piv:PIVPostProcessing')
class PIVPreProcessing(PIVProcessingStep):
    """Pydantic Model for piv:PIVPreProcessing"""


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVEvaluation='piv:PIVEvaluation')
class PIVEvaluation(PIVProcessingStep):
    """Pydantic Model for piv:PIVEvaluation"""


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVMaskGeneration='piv:PIVMaskGeneration')
class PIVMaskGeneration(PIVProcessingStep):
    """Pydantic Model for piv:MaskGeneration"""


# @namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
# @urirefs(ImageRotation='piv:ImageRotation')
# class ImageRotation(PIVProcessingStep):
#     """Pydantic Model for piv:ImageRotation"""


@namespaces(piv='https://matthiasprobst.github.io/pivmeta#')
@urirefs(PIVBackgroundGeneration='piv:PIVBackgroundGeneration')
class PIVBackgroundGeneration(PIVProcessingStep):
    """Pydantic Model for piv:BackgroundImageGeneration"""
