from typing import List, Union

from ontolutils import Thing, namespaces, urirefs
from .variable import Variable, NumericalVariable


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            schema="https://schema.org/")
@urirefs(Method='m4i:Method',
         description='schema:description',
         hasParameter='m4i:hasParameter')
class Method(Thing):
    """Pydantic Model for m4i:M4IProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    description: str = None
    hasParameter: Union[Variable,
    List[Variable]] = None

    def add_numerical_variable(self,
                               label,
                               hasNumericalValue,
                               hasUnit,
                               hasKindOfQuantity,
                               **kwargs):
        """add numerical variable to tool"""
        var = NumericalVariable(label=label,
                                hasNumericalValue=hasNumericalValue,
                                hasUnit=hasUnit,
                                hasKindOfQuantity=hasKindOfQuantity,
                                **kwargs)

        if self.hasParameter is None:
            self.hasParameter = [var, ]
        elif isinstance(self.hasParameter, list):
            self.hasParameter.append(var)
        else:
            self.hasParameter = [self.hasParameter,
                                 var]
