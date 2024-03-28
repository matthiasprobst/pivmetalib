import abc
from typing import Union, Optional, List

from pydantic import Field

from ontolutils import Thing, namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Variable='m4i:Variable',
         description='m4i:hasVariableDescription',
         symbol='m4i:hasSymbol', )
class Variable(Thing):
    """Pydantic Model for m4i:Variable. Not intended to use for modeling. Use NumericalVariable or Text instead."""
    description: str = None  # M4I.hasVariableDescription
    symbol: Optional[str] = Field(default=None, alias="hasSymbol")  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(TextVariable='m4i:TextVariable',
         value='m4i:hasStringValue')
class TextVariable(Variable):
    """Pydantic Model for m4i:TextVariable"""
    value: str = Field(alias="hasStringValue")


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(NumericalVariable='m4i:NumericalVariable',
         value='m4i:hasNumericalValue',
         unit='m4i:hasUnit',
         quantity_kind='m4i:hasKindOfQuantity')
class NumericalVariable(Variable):
    """Pydantic Model for m4i:NumericalVariable"""
    value: Union[int, float, List[int], List[float]] = Field(alias="hasNumericalValue")
    unit: str = Field(default=None, alias="hasUnit")  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    quantity_kind: str = Field(default=None,
                               alias="hasKindOfQuantity")  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity
