from pydantic import EmailStr
from pydantic import HttpUrl

from ..owl import Thing


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
    _PREFIX = "prov"

    # def _repr_html_(self) -> str:
    #     """Returns the HTML representation of the class"""
    #     return f"{self.__class__.__name__}({self.mbox})"


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

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.first_name} {self.last_name}, {self.mbox})"
