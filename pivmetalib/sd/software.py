from pydantic import HttpUrl, AnyUrl
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


@namespaces(schema="http://schema.org/",
            sd="https://w3id.org/okn/o/sd#")
@urirefs(Software='sd:Software',
         short_description='sd:shortDescription',
         has_documentation='sd:hasDocumentation',
         has_download_URL='schema:downloadURL',
         author='schema:author',
         has_source_code='sd:hasSourceCode')
class Software(schema.SoftwareApplication):
    """Pdyantic implementation of sd:Software (https://w3id.org/okn/o/sd#Software)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    short_description: str = None
    has_documentation: AnyUrl = None
    has_download_URL: HttpUrl = None
    author: Union[Person, Organization, List[Union[Person, Organization]]] = None
    has_source_code: SourceCode = None
