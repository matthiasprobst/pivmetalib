from typing import Optional

from ontolutils import namespaces, urirefs
from ontolutils.ex.m4i import Tool
from ontolutils.ex.schema import SoftwareSourceCode
from pydantic import field_validator, Field

from pivmetalib import sd


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OpticalComponent='piv:OpticalComponent')
class OpticalComponent(Tool):
    """Implementation of piv:OpticalComponent"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(LensSystem='piv:LensSystem')
class LensSystem(OpticalComponent):
    """Implementation of piv:LensSystem"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Objective='piv:Objective')
class Objective(LensSystem):
    """Implementation of piv:LensSystem"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Lens='piv:Lens')
class Lens(OpticalComponent):
    """Implementation of piv:Lens"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(LightSource='piv:LightSource')
class LightSource(OpticalComponent):
    """Implementation of piv:LightSource"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Laser='piv:Laser')
class Laser(LightSource):
    """Implementation of piv:Laser"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVSoftware='piv:PIVSoftware')
class PIVSoftware(Tool, sd.Software):
    """Pydantic implementation of piv:PIVSoftware

    PIVSoftware is a m4i:Tool. As m4i:Tool does not define properties,
    sd:Software is used as a dedicated Software description ontology
    """


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OpticSensor='piv:OpticSensor')
class OpticSensor(OpticalComponent):
    """Implementation of piv:LightSource"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Camera='piv:Camera',
         fnumber="piv:fnumber")
class Camera(OpticSensor):
    """Implementation of piv:Camera"""
    fnumber: str = Field(alisas="fstop", default=None)

    @field_validator('fnumber', mode='before')
    @classmethod
    def _fnumber(cls, fnumber):
        return str(fnumber)


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(DigitalCamera="piv:DigitalCamera")
class DigitalCamera(Camera):
    """Pydantic implementation of piv:DigitalCamera"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualCamera="piv:VirtualCamera",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualCamera(DigitalCamera):
    """Pydantic implementation of piv:VirtualCamera"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualLaser="piv:VirtualLaser",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualLaser(LightSource):
    """Pydantic implementation of piv:VirtualLaser"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVParticle="piv:PIVParticle")
class PIVParticle(Tool):
    """Pydantic implementation of piv:Particle"""


setattr(PIVParticle, 'DEHS', 'https://www.wikidata.org/wiki/Q4387284')


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(SyntheticPIVParticle="piv:SyntheticPIVParticle",
         hasSourceCode="codemeta:hasSourceCode")
class SyntheticPIVParticle(Tool):
    """Pydantic implementation of piv:SyntheticParticle"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(NdYAGLaser="piv:NdYAGLaser")
class NdYAGLaser(Laser):
    """Implementation of piv:NdYAGLaser"""
