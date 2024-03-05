from .. import namespaces, urirefs
from ontolutils import Thing


@namespaces(skos="http://www.w3.org/2004/02/skos/core#")
@urirefs(Concept='skos:Concept')
class Concept(Thing):
    """Implementation of skos:Concept"""
