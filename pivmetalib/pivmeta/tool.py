from typing import Union, List, Tuple, Optional

from ontolutils import namespaces, urirefs, QUDT_KIND
from pydantic import field_validator, Field, HttpUrl

from .variable import NumericalVariable
from .. import sd, m4i
from ..m4i.variable import NumericalVariable as M4iNumericalVariable
from ..m4i.variable import TextVariable
from ..namespace import PIVMETA
from ..prov import Organization
from ..schema import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(PivMetaTool='pivmeta:PivMetaTool',
         hasParameter='m4i:hasParameter',
         manufacturer='pivmeta:manufacturer')
class PivMetaTool(m4i.Tool):
    hasParameter: Union[
        TextVariable,
        NumericalVariable,
        M4iNumericalVariable,
        List[Union[TextVariable, NumericalVariable, M4iNumericalVariable]]
    ] = Field(default=None, alias="parameter")
    manufacturer: Organization = None


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


from ssnolib.pimsii import Property


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(DigitalCamera="pivmeta:DigitalCamera",
         fnumber="pivmeta:fnumber")
class DigitalCamera(PIVHardware):
    """Pydantic implementation of pivmeta:DigitalCamera"""
    fnumber: str = None
    sensor_pixel_width: Optional[Union[int, float, Property]]
    sensor_pixel_height: Optional[Union[int, float, Property]]

    @field_validator('sensor_pixel_width', mode='before')
    @classmethod
    def _sensor_pixel_width(cls, sensor_pixel_width: Union[int, Property]):
        if isinstance(sensor_pixel_width, (int, float)):
            return Property(label="sensor_pixel_width",
                            hasValue=sensor_pixel_width,
                            hasStandardName=PIVMETA.sensor_pixel_width)
        return sensor_pixel_width

    @field_validator('sensor_pixel_height', mode='before')
    @classmethod
    def _sensor_pixel_height(cls, sensor_pixel_height: Union[int, Property]):
        if isinstance(sensor_pixel_height, (int, float)):
            return Property(label="sensor_pixel_height",
                            hasValue=sensor_pixel_height,
                            hasStandardName=PIVMETA.sensor_pixel_height)
        return sensor_pixel_height

    # name: str = None
    # cameraType: str = None
    # resolution: ResolutionType = None
    # focalLength: m4i.NumericalVariable = None
    # fnumber: FStopType = None
    # ccdWidth: Property = None
    # ccdHeight: m4i.NumericalVariable = None
    # ccdSize: m4i.NumericalVariable = None

    @field_validator('fnumber', mode='before')
    @classmethod
    def _fnumber(cls, fnumber):
        return str(fnumber)

    # def easy_init(
    #         self,
    #         label: str):
    #     return DigitalCamera()

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
            'parameter': []
        }
        cam_param['parameter'].append(
            NumericalVariable(
                value=focal_length_mm,
                unit='mm',
                quantity_kind=QUDT_KIND.Length,
                standard_name="https://matthiasprobst.github.io/pivmeta#focal_length",
            )
        )
        if sensor_pixel_size is not None:
            w, h = sensor_pixel_size
            cam_param['parameter'].append(
                NumericalVariable(
                    label="sensor_pixel_width",
                    value=w,
                    standard_name="https://matthiasprobst.github.io/pivmeta#sensor_pixel_width")
            )
            cam_param['parameter'].append(
                NumericalVariable(
                    label="sensor_pixel_height",
                    value=h,
                    standard_name="https://matthiasprobst.github.io/pivmeta#sensor_pixel_height")
            )
        if ccd_pixel_size_um is not None:
            if isinstance(ccd_pixel_size_um, (float, int)):
                ccd_pixel_size_um = (ccd_pixel_size_um, ccd_pixel_size_um)
            w, h = ccd_pixel_size_um
            cam_param['parameter'].append(
                NumericalVariable(
                    label="ccd_pixel_width",
                    value=w,
                    unit='um',
                    quantity_kind=QUDT_KIND.Length,
                    standard_name="https://matthiasprobst.github.io/pivmeta#ccd_width")
            )
            cam_param['parameter'].append(
                NumericalVariable(
                    label="ccd_pixel_height",
                    value=h,
                    unit='um',
                    quantity_kind=QUDT_KIND.Length,
                    standard_name="https://matthiasprobst.github.io/pivmeta#ccd_height")
            )
        for k, v in kwargs.items():
            if isinstance(v, (int, float)):
                cam_param['parameter'].append(
                    NumericalVariable(
                        label=k,
                        value=v,
                    )
                )
            elif isinstance(v, str):
                cam_param['parameter'].append(
                    TextVariable(
                        label=k,
                        value=v,
                    )
                )
            else:
                raise TypeError(f'Unsupported type for parameter "{k}": {type(v)}')
        return cls.model_validate(cam_param)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(DigitalCameraModel="pivmeta:DigitalCameraModel",
         source_code="codemeta:hasSourceCode")
class DigitalCameraModel(DigitalCamera):
    """Pydantic implementation of pivmeta:DigitalCameraModel"""
    source_code: Optional[SoftwareSourceCode] = None


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(LaserModel="pivmeta:LaserModel",
         source_code="codemeta:hasSourceCode")
class LaserModel(Laser):
    """Pydantic implementation of pivmeta:LaserModel"""
    source_code: Optional[SoftwareSourceCode] = None


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Particle="pivmeta:Particle",
         material="pivmeta:material")
class Particle(PIVHardware):
    """Pydantic implementation of pivmeta:Particle"""
    material: HttpUrl = None


setattr(Particle, 'DEHS', 'https://www.wikidata.org/wiki/Q4387284')


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(SyntheticParticle="pivmeta:SyntheticParticle",
         source_code="codemeta:hasSourceCode")
class SyntheticParticle(Particle):
    """Pydantic implementation of pivmeta:SyntheticParticle"""
    source_code: Optional[SoftwareSourceCode] = None
