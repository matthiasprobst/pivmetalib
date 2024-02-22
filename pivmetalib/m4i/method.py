from typing import List, Union

from .variable import Variable, NumericalVariable
from .. import Thing
from ..template import namespaces, context


@namespaces(m4i="https://pivmeta.github.io/pivmeta/m4i/",
            schema="https://schema.org/")
@context(Method='m4i:Method',
         description='schema:description',
         has_parameter='m4i:hasParameter')
class Method(Thing):
    """Pydantic Model for m4i:M4IProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    tbd
    """
    description: str = None
    has_parameter: Union[Variable,
                         List[Variable]] = None
    _PREFIX = 'm4i'

    def add_numerical_variable(self, name, has_numerical_value,
                               has_unit, has_kind_of_quantity,
                               **kwargs):
        """add numerical variable to tool"""
        var = NumericalVariable(name=name,
                                has_numerical_value=has_numerical_value,
                                has_unit=has_unit,
                                has_kind_of_quantity=has_kind_of_quantity,
                                **kwargs)

        if self.has_parameter is None:
            self.has_parameter = [var, ]
        elif isinstance(self.has_parameter, list):
            self.has_parameter.append(var)
        else:
            self.has_parameter = [self.has_parameter,
                                  var]
