from typing import Union, List

from .variable import Variable, NumericalVariable
from ..owl import Thing
from .. import namespaces, urirefs


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Tool='m4i:Tool',
         hasParameter='m4i:hasParameter')
class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    hasParameter: Union[Variable, List[Variable]] = None

    def add_numerical_variable(self, numerical_variable: NumericalVariable):
        """add numerical variable to tool"""

        if self.hasParameter is None:
            self.hasParameter = [numerical_variable, ]
        elif isinstance(self.hasParameter, list):
            self.hasParameter.append(numerical_variable)
        else:
            self.hasParameter = [self.hasParameter,
                                  numerical_variable]
