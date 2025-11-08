from datetime import datetime, date
from typing import Optional, Union, List

from ontolutils import namespaces, urirefs
from ontolutils.ex.m4i import TextVariable
from pydantic import Field
from ssnolib.m4i import NumericalVariable

@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(TemporalVariable='pivmeta:TemporalVariable',
         timeValue='pivmeta:timeValue')
class TemporalVariable(TextVariable):
    """A variable with a canonical time value (date or dateTimeStamp) given in piv:timeValue."""
    timeValue: Optional[Union[datetime, date, Union[List[date]], List[datetime]]] = Field(
        default=None,
        description="The canonical time value associated with this temporal variable.",
        alias="time_value"
    )

@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(FlagStatistics='pivmeta:FlagStatistics')
class FlagStatistics(NumericalVariable):
    """Holds statistics, e.g. the number of data points associated with a Flag Variable."""

@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(FlagVariable='pivmeta:FlagVariable',
         hasFlagMeaning='pivmeta:hasFlagMeaning',
         hasFlagValue='pivmeta:hasFlagValue')
class FlagVariable(NumericalVariable):
    """Holds statistics, e.g. the number of data points associated with a Flag Variable."""
    hasFlagMeaning: Optional[str] = Field(
        default=None,
        description="The meaning of the flag value.",
        alias="has_flag_meaning"
    )
    hasFlagValue: Optional[int] = Field(
        default=None,
        description="The integer value of the flag.",
        alias="has_flag_value"
    )
