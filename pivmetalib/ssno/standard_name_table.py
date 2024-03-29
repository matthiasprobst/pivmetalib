import pathlib
from datetime import datetime
from typing import List, Union, Dict

from pydantic import field_validator, Field

from ontolutils import namespaces, urirefs
from . import plugins
from .standard_name import StandardName
from ..dcat import Dataset, Distribution


@namespaces(ssno="https://matthiasprobst.github.io/ssno#")
@urirefs(StandardNameTable='ssno:StandardNameTable',
         standard_names='ssno:hasStandardNames')
class StandardNameTable(Dataset):
    """Implementation of ssno:StandardNameTable

    Parameters
    ----------
    title: str
        Title of the Standard Name Table (dcterms:title)
    description: str
        Description of the Standard Name Table (dcterms:description)
    contact: str
        Contact Person (http://www.w3.org/ns/prov#Person)
    modified: datetime
        Date of the last modification of the Standard Name Table (dcterms:modified)
    version: str
        Version of the Standard Name Table (dcat:version)
    identifier: str
        Identifier of the Standard Name Table, e.g. the DOI (dcterms:identifier)
    standard_names: List[StandardName]
        List of Standard Names (ssno:standard_name)

    """
    standard_names: List[StandardName] = Field(default=None, alias="hasStandardNames")  # ssno:has_standard_names

    def __str__(self) -> str:
        return f'{self.__class__.__name__}("{self.title}")'

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        urls = ', '.join(f'<a href="{d.downloadURL}">{d.title}</a>' for d in self.distribution)
        return f"{self.__class__.__name__}({urls})"

    @classmethod
    def parse(cls,
              source: Union[str, pathlib.Path, Distribution],
              fmt: str = None):
        """Call the reader plugin for the given format.
        Format will select the reader plugin to use. Currently 'xml' is supported."""
        if isinstance(source, (str, pathlib.Path)):
            filename = source
            if fmt is None:
                filename = source
                fmt = pathlib.Path(source).suffix[1:].lower()
        else:
            if fmt is None:
                fmt = source.mediaType
            filename = source.download()
        reader = plugins.get(fmt, None)
        if reader is None:
            raise ValueError(
                f'No plugin found for the file. The reader was determined based on the suffix: {fmt}. '
                'You may overwrite this by providing the parameter fmt'
            )

        data: Dict = reader(filename).parse()

        return cls(**data)

    @field_validator('standard_names')
    @classmethod
    def _standard_names(cls, standard_names: Union[StandardName, List[StandardName]]) -> List[StandardName]:
        if not isinstance(standard_names, list):
            return [standard_names]
        return standard_names

    def get_standard_name(self, standard_name: str) -> Union[StandardName, None]:
        """Check if the Standard Name Table has a given standard name. The
        standard name object is returned if found, otherwise None.

        Parameters
        ----------
        standard_name: str
            The standard name to look for

        Returns
        -------
        Union[StandardName, None]
            The standard name object if found, otherwise None
        """
        for sn in self.has_standard_names:
            if sn.standard_name == standard_name:
                return sn
        return
