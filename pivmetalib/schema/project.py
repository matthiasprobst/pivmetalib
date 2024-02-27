from datetime import datetime
from typing import Union, List

from .thing import Thing
from ..prov import Organisation, Person
from ..model import namespaces, context


@namespaces(schema="https://schema.org/")
@context(Project='schema:Research',
         identifier='schema:identifier',
         startDate='schema:startDate',
         endDate='schema:endDate',
         participant='schema:participant')
class Project(Thing):
    """Pydantic Model for schema:Project"""
    identifier: str
    startDate: datetime
    endDate: datetime
    participant: Union[Person, Organisation, List[Union[Person, Organisation]]]


@context(ResearchProject='schema:ResearchProject')
class ResearchProject(Project):
    """Pydantic Model for schema:ResearchProject

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.mbox})"
