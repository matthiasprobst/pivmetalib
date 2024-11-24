from typing import Optional, Union, List

from ontolutils import Thing
from ontolutils import namespaces, urirefs
from pydantic import Field

from .tool import SoftwareSourceCode


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(PIVSetup="pivmeta:PIVSetup",
         hasPart="obo:hasPart")
class PIVSetup(Thing):
    """Pydantic implementation of pivmeta:PIVSetup"""
    hasPart: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)


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
