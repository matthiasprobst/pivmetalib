from typing import Optional, Union, List

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import Field

from .tool import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(PIVSetup="pivmeta:PIVSetup",
         BFO_0000051="obo:BFO_0000051")
class PIVSetup(Thing):
    """Pydantic implementation of pivmeta:PIVSetup"""
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualPIVSetup="pivmeta:VirtualPIVSetup",
         hasSourceCode="codemeta:hasSourceCode")
class VirtualPIVSetup(PIVSetup):
    """Pydantic implementation of pivmeta:VirtualPIVSetup"""
    hasSourceCode: Optional[SoftwareSourceCode] = Field(alias="source_code", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ExperimentalPIVSetup="pivmeta:ExperimentalPIVSetup")
class ExperimentalPIVSetup(PIVSetup):
    """Pydantic implementation of pivmeta:ExperimentalPIVSetup"""
