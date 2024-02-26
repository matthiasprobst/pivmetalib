from typing import Union, List

from .variable import Variable, NumericalVariable
from ..owl import Thing
from ..template import namespaces, context


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@context(Tool='m4i:Tool',
         has_parameter='m4i:hasParameter')
class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    has_parameter: Union[Variable, List[Variable]] = None

    def add_numerical_variable(self, numerical_variable: NumericalVariable):
        """add numerical variable to tool"""

        if self.has_parameter is None:
            self.has_parameter = [numerical_variable, ]
        elif isinstance(self.has_parameter, list):
            self.has_parameter.append(numerical_variable)
        else:
            self.has_parameter = [self.has_parameter,
                                  numerical_variable]
