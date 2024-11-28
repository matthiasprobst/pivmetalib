import abc
from datetime import datetime
from typing import Any, List, Union

from ontolutils import Thing, namespaces, urirefs
from pydantic import Field
from pydantic import HttpUrl
from pydantic import field_validator

from .method import Method
from .tool import Tool
from ..schema import ResearchProject


class Assignment(Thing):
    """not yet implemented"""


class Activity(Thing, abc.ABC):
    """m4i:Activity (not intended to use for modeling)"""


OneOrMultiThings = Union[Thing, HttpUrl, str, List[Union[Thing, HttpUrl, str]]]


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            schema="https://schema.org/",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(ProcessingStep='m4i:ProcessingStep',
         start_time='schema:startTime',
         end_time='schema:endTime',
         starts_with='obo:starts_with',
         ends_with='obo:ends_with',
         runtime_assignment='m4i:hasRuntimeAssignment',
         investigates='m4i:investigates',
         usageInstruction='m4i:usageInstruction',
         hasEmployedTool='m4i:hasEmployedTool',
         realizes_method='m4i:realizesMethod',
         hasInput='m4i:hasInput',
         hasOutput='m4i:hasOutput',
         part_of='m4i:partOf',
         precedes='m4i:precedes')
class ProcessingStep(Activity):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    start_time: datetime = Field(default=None, alias="startTime")
    end_time: datetime = Field(default=None, alias="endTime")
    starts_with: Any = None
    ends_with: Any = None
    runtime_assignment: Assignment = Field(default=None, alias="hasRuntimeAssignment")
    investigates: Thing = None
    usageInstruction: str = Field(default=None, alias="usage_instruction")
    hasEmployedTool: Tool = Field(default=None, alias="has_employed_tool")
    realizes_method: Union[Method, List[Method]] = Field(default=None, alias="realizesMethod")
    hasInput: Thing = Field(default=None, alias="has_input")
    hasOutput: OneOrMultiThings = Field(default=None, alias="has_output")
    part_of: Union[ResearchProject, "ProcessingStep"] = Field(default=None, alias="partOf")
    precedes: "ProcessingStep" = None

    @field_validator('hasOutput', 'hasInput', mode='before')
    @classmethod
    def _one_or_multiple_things(cls, value):
        if isinstance(value, list):
            ret_value = []
            for v in value:
                if isinstance(v, Thing):
                    ret_value.append(v)
                else:
                    if v.startswith("_:"):
                        ret_value.append(v)
                    else:
                        ret_value.append(str(HttpUrl(v)))
            return ret_value
        if isinstance(value, Thing):
            return value
        if str(value).startswith("_:"):
            return value
        return str(HttpUrl(value))

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
