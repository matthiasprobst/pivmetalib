from typing import List, Union

from .tool import Tool
from .variable import Variable
from ..owl import Thing


class Method(Thing):
    """Pydantic Model for m4i:M4IProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    description: str = None
    has_parameter: Union[Variable, List[Variable]] = None
