import abc
from datetime import datetime
from typing import Any, List, Union

from pydantic import field_validator

from ontolutils import Thing, namespaces, urirefs
from .method import Method
from .tool import Tool
from ..schema import ResearchProject


class Assignment(Thing):
    """not yet implemented"""


class Activity(Thing, abc.ABC):
    """m4i:Activity (not intended to use for modeling)"""


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            schema="http://schema.org/",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(ProcessingStep='m4i:ProcessingStep',
         startTime='schema:startTime',
         endTime='schema:endTime',
         starts_with='obo:starts_with',
         ends_with='obo:ends_with',
         has_runtime_assignment='m4i:hasRuntimeAssignment',
         investigates='m4i:investigates',
         usageInstruction='m4i:usageInstruction',
         hasEmployedTool='m4i:hasEmployedTool',
         realizesMethod='m4i:realizesMethod',
         hasInput='m4i:hasInput',
         hasOutput='m4i:hasOutput',
         partOf='m4i:partOf',
         precedes='m4i:precedes')
class ProcessingStep(Activity):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    startTime: datetime = None
    endTime: datetime = None
    starts_with: Any = None
    ends_with: Any = None
    has_runtime_assignment: Assignment = None
    investigates: Thing = None
    usageInstruction: str = None
    hasEmployedTool: Tool = None
    realizesMethod: Union[Method, List[Method]] = None
    hasInput: Thing = None
    hasOutput: Thing = None
    partOf: Union[ResearchProject, "ProcessingStep"] = None
    precedes: "ProcessingStep" = None

    @field_validator('starts_with', mode='before')
    @classmethod
    def _starts_with(cls, starts_with):
        return _validate_processing_step(starts_with)

    @field_validator('ends_with', mode='before')
    @classmethod
    def _ends_with(cls, ends_with):
        return _validate_processing_step(ends_with)


def _validate_processing_step(ps) -> ProcessingStep:
    if isinstance(ps, ProcessingStep):
        return ps
    if isinstance(ps, dict):
        return ProcessingStep(**ps)
    raise TypeError("starts_with must be of type ProcessingStep or a dictionary")
