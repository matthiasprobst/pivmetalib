from typing import Optional
from typing import Union, List

from ontolutils import Thing, namespaces, urirefs
from pydantic import Field
from pivmetalib.m4i import NumericalVariable, TextVariable

from ..prov import Organization


@namespaces(m4i="http://w3id.org/nfdi4ing/metadata4ing#",
            pivmeta="https://matthiasprobst.github.io/pivmeta#",
            obo="http://purl.obolibrary.org/obo/")
@urirefs(Tool='m4i:Tool',
         manufacturer='pivmeta:manufacturer',
         hasParameter='m4i:hasParameter',
         BFO_0000051='obo:BFO_0000051')
class Tool(Thing):
    """Pydantic Model for m4i:ProcessingStep

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    hasParameter: TextVariable or NumericalVariable or list of them
        Text or numerical variable
    """
    hasParameter: Union[TextVariable, NumericalVariable,
    List[Union[TextVariable, NumericalVariable]]] = Field(default=None, alias="parameter")
    manufacturer: Organization = Field(default=None)
    BFO_0000051: Optional[Union[Thing, List[Thing]]] = Field(alias="has_part", default=None)

    @property
    def hasPart(self):
        return self.BFO_0000051

    @hasPart.setter
    def hasPart(self, value):
        self.BFO_0000051 = value

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
