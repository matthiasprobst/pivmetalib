from pydantic import EmailStr, HttpUrl
from typing import Union

from ontolutils import Thing, namespaces, urirefs
from ..typing import BlankNodeType


@namespaces(prov="http://www.w3.org/ns/prov#",
            foaf="http://xmlns.com/foaf/0.1/")
@urirefs(Agent='prov:Agent',
         mbox='foaf:mbox')
class Agent(Thing):
    """Pydantic Model for http://www.w3.org/ns/prov#Agent

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


@namespaces(schema='http://schema.org/',
            m4i='http://w3id.org/nfdi4ing/metadata4ing#')
@urirefs(Organisation='prov:Organisation',
         name='foaf:name',
         url='schema:url',
         hasRorId='m4i:hasRorId')
class Organisation(Agent):
    """Pydantic Model for http://www.w3.org/ns/prov#Organisation

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    name: str
        Name of the Organisation (foaf:name)
    url: HttpUrl = None
        URL of the item. From schema:url.
    hasRorId: HttpUrl
        A Research Organization Registry identifier, that points to a research organization
    """
    name: str  # foaf:name
    url: HttpUrl = None
    hasRorId: HttpUrl = None


@namespaces(prov="http://www.w3.org/ns/prov#")
@urirefs(Person='prov:Person',
         firstName='foaf:firstName',
         lastName='foaf:lastName',
         hadRole='prov:hadRole',
         wasRoleIn='prov:wasRoleIn',
         affiliation='schema:affiliation')
class Person(Agent):
    """Pydantic Model for http://www.w3.org/ns/prov#Person

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    firstName: str = None
        First name (foaf:firstName)
    lastName: str = None
        Last name (foaf:lastName)
    hadRole: HttpUrl
        prov:hadRole references the Role (i.e. the function of an entity with respect to an activity)
    wasRoleIn: HttpUrl
        prov:wasRoleIn references the association (e.g. between an agent and an activity) in which a role shall be defined. Inverse property of prov:hadRole.

    Extra fields are possible but not explicitly defined here.
    """
    firstName: str = None  # foaf:firstName
    lastName: str = None  # foaf:lastName
    hadRole: HttpUrl = None  # m4i:role
    wasRoleIn: Union[HttpUrl, BlankNodeType] = None  # m4i:role
    affiliation: Organisation = None
