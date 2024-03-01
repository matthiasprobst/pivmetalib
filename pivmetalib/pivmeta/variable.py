from pydantic import HttpUrl
from ssnolib import StandardName
from typing import Union

from .. import m4i
from .. import namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            ssno="https://matthiasprobst.github.io/ssno#")
@urirefs(NumericalVariable='m4i:NumericalVariable',
         hasStandardName='pivmeta:hasStandardName')
class NumericalVariable(m4i.NumericalVariable):
    """Pydantic Model for pivmeta:NumericalVariable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    hasStandardName: Union[StandardName, HttpUrl]
        The standard name of the variable
    """
    hasStandardName: Union[StandardName, HttpUrl] = None
