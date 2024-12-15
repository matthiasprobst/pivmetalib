from pydantic import HttpUrl, AnyUrl, Field
from typing import Union, List

from .. import schema
from ..prov import Person, Organization
from ontolutils import Thing, namespaces, urirefs


@namespaces(sd="https://w3id.org/okn/o/sd#")
@urirefs(SourceCode='sd:SourceCode')
class SourceCode(schema.SoftwareSourceCode):
    """Pydantic implementation of sd:SourceCode ( https://w3id.org/okn/o/sd#SourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """


@namespaces(schema="https://schema.org/",
            sd="https://w3id.org/okn/o/sd#")
@urirefs(Software='sd:Software',
         shortDescription='sd:shortDescription',
         hasDocumentation='sd:hasDocumentation',
         downloadURL='schema:downloadURL',
         author='schema:author',
         hasSourceCode='sd:hasSourceCode')
class Software(schema.SoftwareApplication):
    """Pdyantic implementation of sd:Software (https://w3id.org/okn/o/sd#Software)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    shortDescription: str = Field(alias="short_description", default=None)
    hasDocumentation: AnyUrl = Field(alias="has_documentation", default=None)
    downloadURL: HttpUrl = Field(alias="has_download_URL", default=None)
    author: Union[Person, Organization, List[Union[Person, Organization]]] = None
    hasSourceCode: SourceCode = Field(alias="has_source_code", default=None)
