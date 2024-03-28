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
         canonical_units='ssno:canonicalUnits',
         quantityKind='ssno:quantityKind',
         standard_name='ssno:standard_name',
         description='dcterms:description',
         standard_name_table='ssno:standard_name_table',
         latexSymbol='ssno:latexSymbol')
class StandardName(Concept):
    """Implementation of ssno:StandardName"""
    canonical_units: Union[HttpUrl, str] = None  # ssno:canonicalUnits
    quantityKind: QuantityKind = None
    standard_name: str = None
    description: str  # dcterms:description
    standard_name_table: Dataset = None  # ssno:standard_name_table (subclass of dcat:Dataset)
    latexSymbol: str = None  # ssno:latexSymbol

    @field_validator("canonical_units")
    @classmethod
    def _parse_unit(cls, canonical_units: Union[HttpUrl, str]) -> str:
        """Parse the canonical_units and return the canonical_units as string."""
        if isinstance(canonical_units, str):
            if canonical_units.startswith('http'):
                return str(HttpUrl(canonical_units))
            try:
                return parse_unit(canonical_units)
            except KeyError:
                raise ValueError(f"Could not parse canonical_units: {canonical_units}.")
        return str(HttpUrl(canonical_units))
