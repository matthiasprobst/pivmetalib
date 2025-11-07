from typing import List, Union
from typing import Optional

from ontolutils import namespaces, urirefs
from ontolutils.ex.m4i import ProcessingStep as BaseProcessingStep
from pydantic import Field

from pivmetalib.sd import Software


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            schema="https://schema.org/",
            obo="http://purl.obolibrary.org/obo/",
            codemeta="https://codemeta.github.io/terms/",
            pivmeta="https://matthiasprobst.github.io/pivmeta#"
            )
@urirefs(ProcessingStep='m4i:ProcessingStep',
         usesSoftware="codemeta:usesSoftware",
         usesAnalysisSoftware="pivmeta:usesAnalysisSoftware",
         usesAcquisitionSoftware="pivmeta:usesAcquisitionSoftware",
         )
class ProcessingStep(BaseProcessingStep):
    usesSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses_software", default=None)
    usesAnalysisSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses analysis software",
                                                                            default=None)
    usesAcquisitionSoftware: Optional[Union[Software, List[Software]]] = Field(alias="uses acquisitions software",
                                                                            default=None)
