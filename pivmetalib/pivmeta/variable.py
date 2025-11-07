from datetime import datetime, date
from typing import Optional, Union, List

from ontolutils import namespaces, urirefs
from ontolutils.ex.m4i import TextVariable
from pydantic import Field


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
