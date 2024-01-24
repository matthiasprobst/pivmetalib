import abc
from datetime import datetime
from pydantic import field_validator
from typing import Any

from .method import Method
from ..schemaorg import ResearchProject
from .tool import Tool
from ..core import Thing


class Assignment(Thing):
    """not yet implemented"""


class Activity(Thing, abc.ABC):
    """m4i:Activity (not intended to use for modeling)"""


class ProcessingStep(Activity):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    label: str
    start_time: datetime = None
    end_time: datetime = None
    starts_with: Any = None
    ends_with: Any = None
    has_runtime_assignment: Assignment = None
    investigates: Thing = None
    usage_instruction: str = None
    has_employed_tool: Tool = None
    realizes_method: Method = None
    has_input: Thing = None
    has_output: Thing = None
    part_of: ResearchProject = None

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

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.mbox})"
