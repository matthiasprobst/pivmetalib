from pydantic import HttpUrl
from typing import Union

from ontolutils import namespaces, urirefs
from .. import m4i
from ..ssno import StandardName


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
    standard_name: Union[StandardName, HttpUrl] = None
