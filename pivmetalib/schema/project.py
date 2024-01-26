from datetime import datetime
from typing import Union, List

from ..owl import Thing
from ..prov import Organisation, Person


class Project(Thing):
    """Pydantic Model for schema:Research"""
    has_project_ID: str
    project_start_date: datetime
    project_end_date: datetime
    project_participant: Union[Person, Organisation, List[Union[Person, Organisation]]]


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
