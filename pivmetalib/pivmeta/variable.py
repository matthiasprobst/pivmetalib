from typing import Union

from ontolutils import namespaces, urirefs
from pydantic import HttpUrl, field_validator, Field
from ssnolib import StandardName

from .. import m4i


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            ssno="https://matthiasprobst.github.io/ssno#",
            pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(NumericalVariable='m4i:NumericalVariable',
         standard_name='pivmeta:hasStandardName')
class NumericalVariable(m4i.NumericalVariable):
    """Pydantic Model for pivmeta:NumericalVariable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    standard_name: Union[StandardName, HttpUrl]
        The standard name of the variable
    """
    standard_name: Union[StandardName, HttpUrl, str] = Field(alias="hasStandardName", default=None)

    @field_validator("standard_name", mode='before')
    @classmethod
    def _parse_standard_name(cls, standard_name) -> Union[StandardName, str]:
        """Return the standard name as a StandardName object else validate
        it with HttpUrl and return it as a string"""
        if isinstance(standard_name, StandardName):
            return standard_name
        return str(HttpUrl(standard_name))
