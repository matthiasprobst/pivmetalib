import abc
from typing import Union, Optional, List

from ontolutils import Thing, namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Variable='m4i:Variable',
         description='m4i:hasVariableDescription',
         symbol='m4i:hasSymbol', )
class Variable(Thing, abc.ABC):
    """Pydantic Model for m4i:Variable. Not intended to use for modeling. Use NumericalVariable or Text instead."""
    description: str = None  # M4I.hasVariableDescription
    symbol: Optional[str] = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(TextVariable='m4i:TextVariable',
         value='m4i:hasStringValue')
class TextVariable(Variable):
    """Pydantic Model for m4i:TextVariable"""
    value: str


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(NumericalVariable='m4i:NumericalVariable',
         value='m4i:hasNumericalValue',
         unit='m4i:hasUnit',
         quantity_kind='m4i:hasKindOfQuantity',
         symbol='m4i:hasSymbol')
class NumericalVariable(Variable):
    """Pydantic Model for m4i:NumericalVariable"""
    value: Union[int, float, List[int], List[float]]
    unit: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    quantity_kind: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity
    symbol: str = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"
