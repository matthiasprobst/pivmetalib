from pydantic import HttpUrl
from ssnolib import StandardName
from typing import Union

from .. import m4i
from .. import namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            ssno="https://matthiasprobst.github.io/ssno#")
@urirefs(NumericalVariable='m4i:NumericalVariable',
         standard_name='ssno:standard_name')
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

    # def dump_jsonld(self, id=None, context=None, exclude_none: bool = True) -> str:
    #     ret = super().dump_jsonld(id=id, context=context, exclude_none=exclude_none)
    #     ret['@type'] = 'm4i:NumericalVariable'
    #     return ret
