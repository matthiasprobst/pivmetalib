from typing import Union, List, Optional

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import field_validator, Field

from .variable import NumericalVariable
from .. import sd, m4i
from ..m4i.variable import NumericalVariable as M4iNumericalVariable
from ..m4i.variable import TextVariable
from ..prov import Organization
from ..schema import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(PIVMetaTool='pivmeta:PIVMetaTool',
         hasParameter='m4i:hasParameter',
         manufacturer='pivmeta:manufacturer',
         BFO_0000051='obo:BFO_0000051')
class PIVMetaTool(m4i.Tool):
    hasParameter: Union[
        TextVariable,
        NumericalVariable,
        M4iNumericalVariable,
        List[Union[TextVariable, NumericalVariable, M4iNumericalVariable]]
    ] = Field(default=None, alias="parameter")
    manufacturer: Organization = None
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(OpticalComponent='pivmeta:OpticalComponent')
class OpticalComponent(PIVMetaTool):
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
class PIVSoftware(PIVMetaTool, sd.Software):
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
@urirefs(DigitalCameraModel="pivmeta:DigitalCameraModel",
         hasSourceCode="codemeta:hasSourceCode")
class DigitalCameraModel(DigitalCamera):
    """Pydantic implementation of pivmeta:DigitalCameraModel"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualLaser="pivmeta:VirtualLaser",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualLaser(LightSource):
    """Pydantic implementation of pivmeta:LaserModel"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(PIVParticle="pivmeta:PIVParticle")
class PIVParticle(PIVMetaTool):
    """Pydantic implementation of pivmeta:Particle"""


setattr(PIVParticle, 'DEHS', 'https://www.wikidata.org/wiki/Q4387284')


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(SyntheticPIVParticle="pivmeta:SyntheticPIVParticle",
         hasSourceCode="codemeta:hasSourceCode")
class SyntheticPIVParticle(PIVMetaTool):
    """Pydantic implementation of pivmeta:SyntheticParticle"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(NdYAGLaser="pivmeta:Laser")
class NdYAGLaser(Laser):
    """Implementation of pivmeta:NdYAGLaser"""
