from typing import Optional, Union, List

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import Field

from pivmetalib.sd import Software


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(Setup="pivmeta:Setup",
         BFO_0000051="obo:BFO_0000051")
class Setup(Thing):
    """Pydantic implementation of pivmeta:Setup"""
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(VirtualSetup="pivmeta:VirtualSetup",
         usesSoftware="codemeta:usesSoftware")
class VirtualSetup(Setup):
    """Pydantic implementation of pivmeta:VirtualSetup"""
    usesSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_software", default=None)


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ExperimentalSetup="pivmeta:ExperimentalSetup")
class ExperimentalSetup(Setup):
    """Pydantic implementation of pivmeta:ExperimentalSetup"""
