from typing import Union, List

from ontolutils import Thing, namespaces, urirefs
from pydantic import HttpUrl, Field, field_validator

from pivmetalib.prov.agent import Person, Organization


@namespaces(prov="http://www.w3.org/ns/prov#",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(Attribution='prov:Attribution',
         agent='prov:agent',
         hadRole='dcat:hadRole')
class Attribution(Thing):
    """Pydantic Model for http://www.w3.org/ns/prov#Agent

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    agent: Agent
        Person or Organization
    hadRole: Role
        Role of the agent
    """
    agent: Union[Person, List[Person], Organization, List[Organization], List[Union[Person, Organization]]]
    hadRole: Union[str, HttpUrl] = Field(alias="had_role", default=None)

    @field_validator('hadRole', mode='before')
    @classmethod
    def _hadRole(cls, hadRole: HttpUrl):
        from ..dcat.role import Role
        if isinstance(hadRole, Role):
            return hadRole
        HttpUrl(hadRole)
        return str(hadRole)

    @field_validator('agent', mode='before')
    @classmethod
    def _agent(cls, agent):
        if isinstance(agent, dict):
            _type = str(agent.get("type", agent.get("@type", "")))
            if "Organization" in _type:
                return Organization(**agent)
            elif "Person" in _type:
                return Person(**agent)
        return agent
