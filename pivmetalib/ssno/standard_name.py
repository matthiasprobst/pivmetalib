import warnings
from typing import Union

from pydantic import HttpUrl, field_validator, Field

from ontolutils import namespaces, urirefs
from ..dcat import Dataset
from ..qudt import QuantityKind, parse_unit
from ..skos import Concept


@namespaces(ssno="https://matthiasprobst.github.io/ssno#",
            dcterms="http://purl.org/dc/terms/",
            dcat="http://www.w3.org/ns/dcat#")
@urirefs(StandardName='ssno:StandardName',
         canonical_units='ssno:canonicalUnits',
         quantity_kind='ssno:quantityKind',
         standard_name='ssno:standard_name',
         description='dcterms:description',
         standard_name_table='ssno:standard_name_table',
         latex_symbol='ssno:latexSymbol')
class StandardName(Concept):
    """Implementation of ssno:StandardName"""
    canonical_units: str = Field(default=None, alias="canonicalUnits")
    quantity_kind: QuantityKind = Field(default=None, alias="quantityKind")
    standard_name: str = None
    description: str  # dcterms:description
    standard_name_table: Dataset = None  # ssno:standard_name_table (subclass of dcat:Dataset)
    latex_symbol: str = Field(default=None, alias="latexSymbol")

    @field_validator("canonical_units", mode='before')
    @classmethod
    def _parse_unit(cls, canonical_units: Union[HttpUrl, str]) -> str:
        """Parse the canonical_units and return the canonical_units as string."""
        if canonical_units is None:
            return parse_unit('dimensionless')
        if isinstance(canonical_units, str):
            if canonical_units.startswith('http'):
                return str(HttpUrl(canonical_units))
            try:
                return str(parse_unit(canonical_units))
            except KeyError:
                warnings.warn(f'Could not parse canonical_units: "{canonical_units}".', UserWarning)
            return str(canonical_units)
        return str(HttpUrl(canonical_units))
