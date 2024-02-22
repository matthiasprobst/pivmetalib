from typing import Union, List

from .variable import Variable, NumericalVariable
from ..owl import Thing
from ..template import namespaces, context


@namespaces(m4i="https://pivmeta.github.io/pivmeta/m4i/")
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
