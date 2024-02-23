from datetime import datetime
from typing import Union, List

from .thing import Thing
from ..prov import Organisation, Person
from ..template import namespaces, context


@namespaces(schema="https://schema.org/")
@context(Project='schema:Research',
         has_project_ID='schema:identifier',
         project_start_date='schema:startDate',
         project_end_date='schema:endDate',
         project_participant='schema:participant')
class Project(Thing):
    """Pydantic Model for schema:Project"""
    has_project_ID: str
    project_start_date: datetime
    project_end_date: datetime
    project_participant: Union[Person, Organisation, List[Union[Person, Organisation]]]


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
