from typing import List, Union

from ontolutils import Thing, namespaces, urirefs
from .variable import Variable, NumericalVariable


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            schema="https://schema.org/")
@urirefs(Method='m4i:Method',
         description='schema:description',
         parameter='m4i:hasParameter')
class Method(Thing):
    """Pydantic Model for m4i:M4IProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    description: str = None
    parameter: Union[Variable, List[Variable]] = None

    def add_numerical_variable(self, numerical_variable: Union[dict, NumericalVariable]):
        """add numerical variable to tool"""
        if isinstance(numerical_variable, dict):
            numerical_variable = NumericalVariable(**numerical_variable)
        if self.parameter is None:
            self.parameter = [numerical_variable, ]
        elif isinstance(self.parameter, list):
            self.parameter.append(numerical_variable)
        else:
            self.parameter = [self.parameter, numerical_variable]
