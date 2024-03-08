import abc
from typing import Union, Optional, List

from ontolutils import Thing, namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Variable='m4i:Variable',
         hasVariableDescription='m4i:hasVariableDescription',
         hasSymbol='m4i:hasSymbol', )
class Variable(Thing, abc.ABC):
    """Pydantic Model for m4i:Variable. Not intended to use for modeling. Use NumericalVariable or Text instead."""
    hasVariableDescription: str = None  # M4I.hasVariableDescription
    hasSymbol: Optional[str] = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"


@urirefs(TextVariable='m4i:TextVariable',
         hasStringValue='m4i:hasStringValue')
class TextVariable(Variable):
    """Pydantic Model for m4i:TextVariable"""
    hasStringValue: str


@urirefs(NumericalVariable='m4i:NumericalVariable',
         hasNumericalValue='m4i:hasNumericalValue',
         hasUnit='m4i:hasUnit',
         hasKindOfQuantity='m4i:hasKindOfQuantity',
         hasSymbol='m4i:hasSymbol')
class NumericalVariable(Variable):
    """Pydantic Model for m4i:NumericalVariable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    hasNumericalValue: Union[int, float, List[int], List[float]]  # M4I.Value
    hasUnit: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    hasKindOfQuantity: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity
    hasSymbol: str = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"
