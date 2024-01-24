from typing import List, Union

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
    label: str
    has_parameter: Union[Variable, List[Variable]] = None

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        return f"{self.__class__.__name__}({self.mbox})"
