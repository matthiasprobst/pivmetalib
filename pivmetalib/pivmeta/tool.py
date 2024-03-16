from typing import Union, List, Tuple, Optional

from pydantic import field_validator

from ontolutils import namespaces, urirefs, QUDT_KIND
from .variable import NumericalVariable
from .. import sd, m4i
from ..m4i.variable import NumericalVariable as M4iNumericalVariable
from ..m4i.variable import TextVariable
from ..schema import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PivMetaTool='pivmeta:PivMetaTool')
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

    @field_validator('fnumber', mode='before')
    @classmethod
    def _fnumber(cls, fnumber):
        return str(fnumber)

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
                    label="sensor_pixel_width",
                    hasNumericalValue=w,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#sensor_pixel_width")
            )
            cam_param['hasParameter'].append(
                NumericalVariable(
                    label="sensor_pixel_height",
                    hasNumericalValue=h,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#sensor_pixel_height")
            )
        if ccd_pixel_size_um is not None:
            if isinstance(ccd_pixel_size_um, (float, int)):
                ccd_pixel_size_um = (ccd_pixel_size_um, ccd_pixel_size_um)
            w, h = ccd_pixel_size_um
            cam_param['hasParameter'].append(
                NumericalVariable(
                    label="ccd_pixel_width",
                    hasNumericalValue=w,
                    hasUnit='um',
                    hasKindOfQuantity=QUDT_KIND.Length,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#ccd_width")
            )
            cam_param['hasParameter'].append(
                NumericalVariable(
                    label="ccd_pixel_height",
                    hasNumericalValue=h,
                    hasUnit='um',
                    hasKindOfQuantity=QUDT_KIND.Length,
                    hasStandardName="https://matthiasprobst.github.io/pivmeta#ccd_height")
            )
        for k, v in kwargs.items():
            if isinstance(v, (int, float)):
                cam_param['hasParameter'].append(
                    NumericalVariable(
                        label=k,
                        hasNumericalValue=v,
                    )
                )
            elif isinstance(v, str):
                cam_param['hasParameter'].append(
                    TextVariable(
                        label=k,
                        hasStringValue=v,
                    )
                )
            else:
                raise TypeError(f'Unsupported type for parameter "{k}": {type(v)}')
        return cls.model_validate(cam_param)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(DigitalCameraModel="pivmeta:DigitalCameraModel",
         hasSourceCode="codemeta:hasSourceCode")
class DigitalCameraModel(DigitalCamera):
    """Pydantic implementation of pivmeta:DigitalCameraModel"""
    hasSourceCode: Optional[SoftwareSourceCode] = None


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(LaserModel="pivmeta:LaserModel",
         hasSourceCode="codemeta:hasSourceCode")
class LaserModel(Laser):
    """Pydantic implementation of pivmeta:LaserModel"""
    hasSourceCode: Optional[SoftwareSourceCode] = None


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Particle="pivmeta:Particle")
class Particle(PIVHardware):
    """Pydantic implementation of pivmeta:Particle"""
    pass


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(SyntheticParticle="pivmeta:SyntheticParticle",
         hasSourceCode="codemeta:hasSourceCode")
class SyntheticParticle(Particle):
    """Pydantic implementation of pivmeta:SyntheticParticle"""
    hasSourceCode: Optional[SoftwareSourceCode] = None
