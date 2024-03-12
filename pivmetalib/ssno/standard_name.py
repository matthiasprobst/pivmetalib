from typing import Union

from pydantic import HttpUrl, field_validator

from ontolutils import namespaces, urirefs
from ..dcat import Dataset
from ..qudt import QuantityKind, parse_unit
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
    unit: Union[HttpUrl, str] = None  # ssno:unit
    quantityKind: QuantityKind = None
    standard_name: str = None
    description: str  # dcterms:description
    standard_name_table: Dataset = None  # ssno:standard_name_table (subclass of dcat:Dataset)
    latexSymbol: str = None  # ssno:latexSymbol

    @field_validator("unit")
    @classmethod
    def _parse_unit(cls, unit: Union[HttpUrl, str]) -> str:
        """Parse the unit and return the unit as string."""
        if isinstance(unit, str):
            if unit.startswith('http'):
                return str(HttpUrl(unit))
            return str(parse_unit(unit))
        return str(HttpUrl(unit))
