from typing import Union, Optional

from ..owl import Thing


class Variable(Thing):
    """Pydantic Model for m4i:Variable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    value: Union[int, float]  # M4I.Value
    description: str = None  # M4I.hasVariableDescription
    has_unit: str = None  # http://w3id.org/nfdi4ing/metadata4ing#hasUnit
    has_kind_of_quantity: Optional[str] = None  # http://w3id.org/nfdi4ing/metadata4ing#hasKindOfQuantity
    has_symbol: Optional[str] = None  # "http://w3id.org/nfdi4ing/metadata4ing#hasSymbol"
