from typing import Optional, Union, List

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import Field

from pivmetalib.sd import Software


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/",
            codemeta="https://codemeta.github.io/terms/")
@urirefs(Setup="piv:Setup",
         BFO_0000051="obo:BFO_0000051",
         usesSoftware="codemeta:usesSoftware",
         usesAnalysisSoftware="piv:usesAnalysisSoftware",
         usesAcquisitionSoftware="piv:usesAcquisitionSoftware",
         )
class Setup(Thing):
    """Pydantic implementation of piv:Setup"""
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)
    usesSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_software", default=None)

    usesAnalysisSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_analysis_software",
                                                                            default=None)
    usesAcquisitionSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_acquisitions_software",
                                                                               default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(VirtualSetup="piv:VirtualSetup",
         usesSoftware="codemeta:usesSoftware")
class VirtualSetup(Setup):
    """Pydantic implementation of piv:VirtualSetup"""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(ExperimentalSetup="piv:ExperimentalSetup")
class ExperimentalSetup(Setup):
    """Pydantic implementation of piv:ExperimentalSetup"""
