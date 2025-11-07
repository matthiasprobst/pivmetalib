from typing import Optional, Union, List

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import Field

from pivmetalib.sd import Software


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(Setup="pivmeta:Setup",
         BFO_0000051="obo:BFO_0000051",
         usesSoftware="codemeta:usesSoftware",
         usesAnalysisSoftware="pivmeta:usesAnalysisSoftware",
         usesAcquisitionSoftware="pivmeta:usesAcquisitionSoftware",
         )
class Setup(Thing):
    """Pydantic implementation of pivmeta:Setup"""
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)
    usesSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_software", default=None)

    usesAnalysisSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses analysis software",
                                                                            default=None)
    usesAcquisitionSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses acquisitions software",
                                                                               default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(VirtualSetup="pivmeta:VirtualSetup",
         usesSoftware="codemeta:usesSoftware")
class VirtualSetup(Setup):
    """Pydantic implementation of pivmeta:VirtualSetup"""


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ExperimentalSetup="pivmeta:ExperimentalSetup")
class ExperimentalSetup(Setup):
    """Pydantic implementation of pivmeta:ExperimentalSetup"""
