from pydantic import EmailStr

from ..owl import Thing
from ..template import namespaces, context


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


@context(Organisation='prov:Organisation',
         name='foaf:name')
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
    """
    name: str  # foaf:name


@context(Person='prov:Person',
         first_name='foaf:firstName',
         last_name='foaf:lastName')
class Person(Agent):
    """Pydantic Model for https://www.w3.org/ns/prov#Person

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    first_name: str = None
        First name (foaf:firstName)
    last_name: str = None
        Last name (foaf:lastName)
    mbox: EmailStr = None
        Email address (foaf:mbox)

    Extra fields are possible but not explicitly defined here.
    """
    first_name: str = None  # foaf:firstName
    last_name: str = None  # foaf:lastName
