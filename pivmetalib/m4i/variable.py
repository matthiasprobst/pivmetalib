import warnings
from typing import Union, Optional, List

from pydantic import Field, field_validator

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
         hasNumericalValue='m4i:hasNumericalValue',
         hasUnit='m4i:hasUnit',
         hasKindOfQuantity='m4i:hasKindOfQuantity')
class NumericalVariable(Variable):
    """Pydantic Model for m4i:NumericalVariable"""
    hasNumericalValue: Union[int, float, List[int], List[float]] = Field(alias="value")
    hasUnit: str = Field(default=None, alias="unit")  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    hasKindOfQuantity: str = Field(default=None,
                               alias="quantity_kind")  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity

    @field_validator("hasUnit", mode='before')
    @classmethod
    def _parse_unit(cls, unit):
        if unit.startswith("http"):
            return str(unit)
        from ..qudt import parse_unit
        try:
            return parse_unit(unit)
        except KeyError as e:
            warnings.warn(f"Unit '{unit}' could not be parsed to QUDT IRI. This is a process based on a dictionary "
                          f"lookup. Either the unit is wrong or it is not yet included in the dictionary. ")
        return str(unit)
