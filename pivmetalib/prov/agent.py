from ontolutils import Thing, namespaces, urirefs
from pydantic import EmailStr, HttpUrl, Field


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
    mbox: EmailStr = Field(default=None, alias="personal mailbox")  # foaf:mbox

    # def _repr_html_(self) -> str:
    #     """Returns the HTML representation of the class"""
    #     return f"{self.__class__.__name__}({self.mbox})"


@namespaces(schema='https://schema.org/',
            foaf='http://xmlns.com/foaf/0.1/',
            m4i='http://w3id.org/nfdi4ing/metadata4ing#',
            prov='http://www.w3.org/ns/prov#')
@urirefs(Organization='prov:Organization',
         name='foaf:name',
         url='schema:url',
         ror_id='m4i:hasRorId')
class Organization(Agent):
    """Pydantic Model for http://www.w3.org/ns/prov#Organization

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    name: str
        Name of the Organization (foaf:name)
    url: HttpUrl = None
        URL of the item. From schema:url.
    ror_id: HttpUrl
        A Research Organization Registry identifier, that points to a research organization
    """
    name: str  # foaf:name
    url: HttpUrl = None
    ror_id: HttpUrl = Field(alias="hasRorId", default=None)


@namespaces(prov="http://www.w3.org/ns/prov#",
            foaf="http://xmlns.com/foaf/0.1/",
            m4i='http://w3id.org/nfdi4ing/metadata4ing#',
            schema="https://schema.org/")
@urirefs(Person='prov:Person',
         firstName='foaf:firstName',
         lastName='foaf:lastName',
         orcidId='m4i:orcidId',
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
    orcidId: str = None
        ORCID ID of person (m4i:orcidID)

    Extra fields are possible but not explicitly defined here.
    """
    firstName: str = Field(default=None, alias="first_name")  # foaf:first_name
    lastName: str = Field(default=None, alias="last_name")  # foaf:last_name
    orcidId: str = Field(default=None, alias="orcid_id")  # m4i:orcidID
    # had_role: HttpUrl = Field(default=None, alias="hadRole")  # m4i:hadRole
    # was_role_in: Union[HttpUrl, str, Thing] = Field(default=None, alias="wasRoleIn")  # m4i:wasRoleIn
    affiliation: Organization = Field(default=None, alias="affiliation")  # schema:affiliation
