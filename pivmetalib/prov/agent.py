from pydantic import EmailStr, HttpUrl

from ..owl import Thing
from ..model import namespaces, context


@namespaces(prov="https://www.w3.org/ns/prov#",
            foaf="http://xmlns.com/foaf/0.1/")
@context(Agent='prov:Agent',
         mbox='foaf:mbox')
class Agent(Thing):
    """Pydantic Model for https://www.w3.org/ns/prov#Agent

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    mbox: EmailStr = None
        Email address (foaf:mbox)
    """
    mbox: EmailStr = None  # foaf:mbox

    # def _repr_html_(self) -> str:
    #     """Returns the HTML representation of the class"""
    #     return f"{self.__class__.__name__}({self.mbox})"


@namespaces(schema='http://schema.org/')
@context(Organisation='prov:Organisation',
         name='foaf:name',
         url='schema:url'
         )
class Organisation(Agent):
    """Pydantic Model for https://www.w3.org/ns/prov#Organisation

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    name: str
        Name of the Organisation (foaf:name)
    mbox: EmailStr = None
        Email address (foaf:mbox)
    url: str = None
    """
    name: str  # foaf:name
    url: HttpUrl = None


@context(Person='prov:Person',
         firstName='foaf:firstName',
         lastName='foaf:lastName')
class Person(Agent):
    """Pydantic Model for https://www.w3.org/ns/prov#Person

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    firstName: str = None
        First name (foaf:firstName)
    lastName: str = None
        Last name (foaf:lastName)
    mbox: EmailStr = None
        Email address (foaf:mbox)

    Extra fields are possible but not explicitly defined here.
    """
    firstName: str = None  # foaf:firstName
    lastName: str = None  # foaf:lastName
