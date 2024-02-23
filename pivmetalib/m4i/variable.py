import abc
from typing import Union, Optional

from ..owl import Thing
from ..template import namespaces, context


@namespaces(m4i="https://pivmeta.github.io/pivmeta/m4i/")
@context(Variable='m4i:Variable',
         has_variable_description='m4i:hasVariableDescription',
         has_symbol='m4i:hasSymbol', )
class Variable(Thing, abc.ABC):
    """Pydantic Model for m4i:Variable. Not intended to use for modeling. Use NumericalVariable or Text instead."""
    has_variable_description: str = None  # M4I.hasVariableDescription
    has_symbol: Optional[str] = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"


@context(TextVariable='m4i:TextVariable',
         has_string_value='m4i:hasStringValue')
class TextVariable(Variable):
    """Pydantic Model for m4i:TextVariable"""
    has_string_value: str


@context(NumericalVariable='m4i:NumericalVariable',
         has_numerical_value='m4i:hasNumericalValue',
         has_unit='m4i:hasUnit',
         has_kind_of_quantity='m4i:hasKindOfQuantity',
         has_symbol='m4i:hasSymbol')
class NumericalVariable(Variable):
    """Pydantic Model for m4i:NumericalVariable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    has_numerical_value: Union[int, float]  # M4I.Value
    has_unit: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    has_kind_of_quantity: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity
    has_symbol: str = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"
