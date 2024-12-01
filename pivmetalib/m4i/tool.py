from typing import Union, List
from pydantic import Field
from ontolutils import Thing, namespaces, urirefs
from .variable import NumericalVariable, TextVariable


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#")
@urirefs(Tool='m4i:Tool',
         hasParameter='m4i:hasParameter')
class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    parameter: TextVariable or NumericalVariable or list of them
        Text or numerical variable
    """
    hasParameter: Union[TextVariable, NumericalVariable,
    List[Union[TextVariable, NumericalVariable]]] = Field(default=None, alias="parameter")

    def add_numerical_variable(self, numerical_variable: Union[dict, NumericalVariable]):
        """add numerical variable to tool"""
        if isinstance(numerical_variable, dict):
            numerical_variable = NumericalVariable(**numerical_variable)
        if self.parameter is None:
            self.hasParameter = [numerical_variable, ]
        elif isinstance(self.hasParameter, list):
            self.hasParameter.append(numerical_variable)
        else:
            self.hasParameter = [self.hasParameter,
                                 numerical_variable]
