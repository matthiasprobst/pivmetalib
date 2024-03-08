from ontolutils import Thing, namespaces, urirefs
from ..dcat import Dataset
from ..qudt import Unit, QuantityKind
from ..skos import Concept


@namespaces(ssno="https://matthiasprobst.github.io/ssno#",
            dcterms="http://purl.org/dc/terms/",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(StandardName='ssno:StandardName',
         unit='ssno:unit',
         quantityKind='ssno:quantityKind',
         standard_name='ssno:standard_name',
         description='dcterms:description',
         standard_name_table='ssno:standard_name_table',
         latexSymbol='ssno:latexSymbol')
class StandardName(Concept):
    """Implementation of ssno:StandardName"""
    unit: Unit = None
    quantityKind: QuantityKind = None
    standard_name: str = None
    description: str  # dcterms:description
    standard_name_table: Dataset = None  # ssno:standard_name_table (subclass of dcat:Dataset)
    latexSymbol: str = None  # ssno:latexSymbol
