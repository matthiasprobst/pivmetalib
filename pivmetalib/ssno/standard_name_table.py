import pathlib
from datetime import datetime
from typing import List, Union, Dict

from . import plugins
from .standard_name import StandardName
from ..dcat import Dataset, Distribution


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
    standard_names: List[StandardName] = None  # ssno:standard_name

    def __str__(self):
        return f'{self.title}'

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        urls = ', '.join(f'<a href="{d.downloadURL}">{d.title}</a>' for d in self.distribution)
        return f"{self.__class__.__name__}({urls})"

    @classmethod
    def parse(cls,
              source: Union[str, pathlib.Path, Distribution],
              format=None):
        """Call the reader plugin for the given format.
        Format will select the reader plugin to use. Currently 'xml' is supported."""
        if isinstance(source, (str, pathlib.Path)):
            filename = source
            if format is None:
                filename = source
                format = pathlib.Path(source).suffix[1:].lower()
                if format not in plugins:
                    raise ValueError(
                        f'No plugin found for the file. The reader was determined based on the suffix: {format}. '
                        'You may overwrite this by providing the parameter format'
                    )
        else:
            if format is None:
                format = source.mediaType
            filename = source.download()

        Reader = plugins.get(format)
        data: Dict = Reader(filename).parse()

        return cls(**data)
