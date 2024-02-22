import abc
from datetime import datetime
from pydantic import field_validator
from typing import Any, List, Union

from .method import Method
from .tool import Tool
from ..owl import Thing
from ..schema import ResearchProject
from ..template import namespaces, context


class Assignment(Thing):
    """not yet implemented"""
    _PREFIX = 'm4i'


class Activity(Thing, abc.ABC):
    """m4i:Activity (not intended to use for modeling)"""
    _PREFIX = 'm4i'


@namespaces(m4i="https://pivmeta.github.io/pivmeta/m4i/")
@context(ProcessingStep='m4i:ProcessingStep',
         has_runtime_assignment='m4i:hasRuntimeAssignment',
         investigates='m4i:investigates',
         usage_instruction='m4i:usageInstruction',
         has_employed_tool='m4i:hasEmployedTool',
         realizes_method='m4i:realizesMethod',
         has_input='m4i:hasInput',
         has_output='m4i:hasOutput',
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
    start_time: datetime = None
    end_time: datetime = None
    starts_with: Any = None
    ends_with: Any = None
    has_runtime_assignment: Assignment = None
    investigates: Thing = None
    usage_instruction: str = None
    has_employed_tool: Tool = None
    realizes_method: Union[Method, List[Method]] = None
    has_input: Thing = None
    has_output: Thing = None
    part_of: Union[ResearchProject, "ProcessingStep"] = None
    precedes: "ProcessingStep" = None

    @field_validator('starts_with', mode='before')
    @classmethod
    def _starts_with(cls, starts_with):
        if isinstance(starts_with, cls):
            return starts_with
        if isinstance(starts_with, dict):
            return ProcessingStep(**starts_with)
        raise TypeError("starts_with must be of type ProcessingStep or a dictionary")

    @field_validator('ends_with', mode='before')
    @classmethod
    def _ends_with(cls, ends_with):
        if isinstance(ends_with, cls):
            return ends_with
        if isinstance(ends_with, dict):
            return ProcessingStep(**ends_with)
        raise TypeError("ends_with must be of type ProcessingStep or a dictionary")
