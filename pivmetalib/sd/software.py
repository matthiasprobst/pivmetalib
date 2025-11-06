import pathlib
from typing import Union, List

from ontolutils import namespaces, urirefs, get_urirefs, dquery
from pydantic import HttpUrl, AnyUrl, Field

from ontolutils.ex.prov import Person, Organization
from ontolutils.ex.schema import SoftwareSourceCode, SoftwareApplication


@namespaces(sd="https://w3id.org/okn/o/sd#")
@urirefs(SourceCode='sd:SourceCode')
class SourceCode(SoftwareSourceCode):
    """Pydantic implementation of sd:SourceCode ( https://w3id.org/okn/o/sd#SourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """

    @classmethod
    def from_codemeta(cls, filename: Union[str, pathlib.Path]) -> SoftwareSourceCode:
        """Create a SoftwareSourceCode instance from a codemeta.json file."""
        import json
        from ontolutils.classes.utils import download_file

        # get codemeta context file:
        codemeta_context_file = download_file(
            'https://raw.githubusercontent.com/codemeta/codemeta/2.0/codemeta.jsonld',
            None)
        with open(codemeta_context_file) as f:
            codemeta_context = json.load(f)['@context']

        with open(filename, encoding='utf-8') as f:
            data = json.load(f)
            # ssc = SoftwareSourceCode.from_jsonld(data=data)

        # replace context in data
        _ = data.pop('@context')
        data['@context'] = codemeta_context

        return SoftwareSourceCode.from_jsonld(data=json.dumps(data), limit=1)



@namespaces(schema="https://schema.org/",
            sd="https://w3id.org/okn/o/sd#")
@urirefs(Software='sd:Software',
         shortDescription='sd:shortDescription',
         hasDocumentation='sd:hasDocumentation',
         downloadURL='schema:downloadURL',
         author='schema:author',
         hasSourceCode='sd:hasSourceCode')
class Software(SoftwareApplication):
    """Pdyantic implementation of sd:Software (https://w3id.org/okn/o/sd#Software)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    shortDescription: str = Field(alias="short_description", default=None)
    hasDocumentation: AnyUrl = Field(alias="has_documentation", default=None)
    downloadURL: HttpUrl = Field(alias="has_download_URL", default=None)
    author: Union[Person, Organization, List[Union[Person, Organization]]] = Field(default=None)
    hasSourceCode: Union[SourceCode, SoftwareSourceCode] = Field(alias="has_source_code", default=None)
