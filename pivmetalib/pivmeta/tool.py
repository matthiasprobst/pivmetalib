from typing import Union, List, Tuple

from ontolutils import QUDT_KIND

from .variable import NumericalVariable
from .. import namespaces, urirefs
from .. import sd, m4i
from ..m4i.variable import NumericalVariable as M4iNumericalVariable
from ..m4i.variable import TextVariable

class PivMetaTool(m4i.Tool):
    hasParameter: Union[
        TextVariable,
        NumericalVariable,
        M4iNumericalVariable,
        List[Union[TextVariable, NumericalVariable, M4iNumericalVariable]]
    ] = None


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVSoftware='pivmeta:PIVSoftware')
class PIVSoftware(PivMetaTool, sd.Software):
    """Pydantic implementation of pivmeta:PIVSoftware

    PIVSoftware is a m4i:Tool. As m4i:Tool does not define properties,
    sd:Software is used as a dedicated Software description ontology
    """


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVHardware='pivmeta:PIVHardware')
class PIVHardware(PivMetaTool):
    """Pydantic implementation of pivmeta:PIVHardware"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Laser='pivmeta:Laser')
class Laser(PIVHardware):
    """Pydantic implementation of pivmeta:Laser"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(DigitalCamera="pivmeta:DigitalCamera",
         fnumber="pivmeta:fnumber")
class DigitalCamera(PIVHardware):
    """Pydantic implementation of pivmeta:DigitalCamera"""
    fnumber: str = None

    # name: str = None
    # cameraType: str = None
    # resolution: ResolutionType = None
    # focalLength: m4i.NumericalVariable = None
    # fnumber: FStopType = None
    # ccdWidth: m4i.NumericalVariable = None
    # ccdHeight: m4i.NumericalVariable = None
    # ccdSize: m4i.NumericalVariable = None

    @classmethod
    def build_minimal(cls,
                      label: str,
                      sensor_pixel_size: Tuple[int, int],
                      focal_length_mm: float,
                      fnumber: str,
                      ccd_pixel_size_um: Tuple[int, int] = None,
                      **kwargs):
        """Helper class method to quickly build a minimal camera object"""
        cam_param = {
            'label': label,
            'fnumber': fnumber,
            'hasParameter': []
        }
        cam_param['hasParameter'].append(
            NumericalVariable(
                hasNumericalValue=focal_length_mm,
                hasUnit='mm',
                hasKindOfQuantity=QUDT_KIND.Length,
                hasStandardName="https://matthiasprobst.github.io/pivmeta#focal_length",
            )
        )
        if sensor_pixel_size is not None:
            w, h = sensor_pixel_size
            cam_param['hasParameter'].append(
                NumericalVariable(
                    hasNumericalValue=w,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#sensor_pixel_width")
            )
            cam_param['hasParameter'].append(
                NumericalVariable(
                    hasNumericalValue=h,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#sensor_pixel_height")
            )
        if ccd_pixel_size_um is not None:
            w, h = ccd_pixel_size_um
            cam_param['hasParameter'].append(
                NumericalVariable(
                    hasNumericalValue=w,
                    hasUnit='um',
                    hasKindOfQuantity=QUDT_KIND.Length,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#ccd_width")
            )
            cam_param['hasParameter'].append(
                NumericalVariable(
                    hasNumericalValue=h,
                    hasUnit='um',
                    hasKindOfQuantity=QUDT_KIND.Length,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#ccd_height")
            )
        for k, v in kwargs.items():
            if isinstance(v, (int, float)):
                cam_param['hasParameter'].append(
                    NumericalVariable(
                        hasNumericalValue=v,
                    )
                )
            elif isinstance(v, str):
                cam_param['hasParameter'].append(
                    TextVariable(
                        hasStringValue=v,
                    )
                )
            else:
                raise TypeError(f'Unsupported type for parameter "{k}": {type(v)}')
        return cls.model_validate(cam_param)
