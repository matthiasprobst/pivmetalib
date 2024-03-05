from .. import namespaces, urirefs
from ontolutils import Thing


@namespaces(qudt="http://qudt.org/schema/qudt/")
@urirefs(QuantityKind='qudt:QuantityKind')
class QuantityKind(Thing):
    """Implementation of qudt:QuantityKind"""
