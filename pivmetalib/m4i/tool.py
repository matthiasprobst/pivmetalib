from typing import Union, List
from pydantic import Field
from ontolutils import Thing, namespaces, urirefs
from .variable import NumericalVariable, TextVariable


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Tool='m4i:Tool',
         parameter='m4i:hasParameter')
class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    parameter: TextVariable or NumericalVariable or list of them
        Text or numerical variable
    """
    parameter: Union[TextVariable, NumericalVariable,
    List[Union[TextVariable, NumericalVariable]]] = Field(default=None, alias="hasParameter")

    def add_numerical_variable(self, numerical_variable: Union[dict, NumericalVariable]):
        """add numerical variable to tool"""
        if isinstance(numerical_variable, dict):
            numerical_variable = NumericalVariable(**numerical_variable)
        if self.parameter is None:
            self.parameter = [numerical_variable, ]
        elif isinstance(self.parameter, list):
            self.parameter.append(numerical_variable)
        else:
            self.parameter = [self.parameter,
                                 numerical_variable]
