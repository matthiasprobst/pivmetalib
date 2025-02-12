from typing import Optional

from ontolutils import namespaces, urirefs
from pydantic import field_validator, Field

from pivmetalib import sd
from pivmetalib.m4i import Tool
from pivmetalib.schema import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OpticalComponent='pivmeta:OpticalComponent')
class OpticalComponent(Tool):
    """Implementation of pivmeta:OpticalComponent"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(LensSystem='pivmeta:LensSystem')
class LensSystem(OpticalComponent):
    """Implementation of pivmeta:LensSystem"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Objective='pivmeta:Objective')
class Objective(LensSystem):
    """Implementation of pivmeta:LensSystem"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Lens='pivmeta:Lens')
class Lens(OpticalComponent):
    """Implementation of pivmeta:Lens"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(LightSource='pivmeta:LightSource')
class LightSource(OpticalComponent):
    """Implementation of pivmeta:LightSource"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Laser='pivmeta:Laser')
class Laser(LightSource):
    """Implementation of pivmeta:Laser"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVSoftware='pivmeta:PIVSoftware')
class PIVSoftware(Tool, sd.Software):
    """Pydantic implementation of pivmeta:PIVSoftware

    PIVSoftware is a m4i:Tool. As m4i:Tool does not define properties,
    sd:Software is used as a dedicated Software description ontology
    """


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OpticSensor='pivmeta:OpticSensor')
class OpticSensor(OpticalComponent):
    """Implementation of pivmeta:LightSource"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Camera='pivmeta:Camera',
         fnumber="pivmeta:fnumber")
class Camera(OpticSensor):
    """Implementation of pivmeta:Camera"""
    fnumber: str = Field(alisas="fstop", default=None)

    @field_validator('fnumber', mode='before')
    @classmethod
    def _fnumber(cls, fnumber):
        return str(fnumber)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(DigitalCamera="pivmeta:DigitalCamera")
class DigitalCamera(Camera):
    """Pydantic implementation of pivmeta:DigitalCamera"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualCamera="pivmeta:VirtualCamera",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualCamera(DigitalCamera):
    """Pydantic implementation of pivmeta:VirtualCamera"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualLaser="pivmeta:VirtualLaser",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualLaser(LightSource):
    """Pydantic implementation of pivmeta:VirtualLaser"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVParticle="pivmeta:PIVParticle")
class PIVParticle(Tool):
    """Pydantic implementation of pivmeta:Particle"""


setattr(PIVParticle, 'DEHS', 'https://www.wikidata.org/wiki/Q4387284')


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(SyntheticPIVParticle="pivmeta:SyntheticPIVParticle",
         hasSourceCode="codemeta:hasSourceCode")
class SyntheticPIVParticle(Tool):
    """Pydantic implementation of pivmeta:SyntheticParticle"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(NdYAGLaser="pivmeta:NdYAGLaser")
class NdYAGLaser(Laser):
    """Implementation of pivmeta:NdYAGLaser"""
