from .variable import Variable
from ..owl import Thing


class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    label: str = None
    has_parameter: Variable = None
