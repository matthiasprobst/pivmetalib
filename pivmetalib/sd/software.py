from pydantic import HttpUrl, AnyUrl
from typing import Union, List

from .. import schema
from ..prov import Person, Organisation
from ..model import namespaces, context


@namespaces(sd="https://w3id.org/okn/o/sd#")
@context(SourceCode='sd:SourceCode')
class SourceCode(schema.SoftwareSourceCode):
    """Pydantic implementation of sd:SourceCode ( https://w3id.org/okn/o/sd#SourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """


@namespaces(schema="https://schema.org/",
            sd="https://w3id.org/okn/o/sd#")
@context(Software='sd:Software',
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
    author: Union[Person, Organisation, List[Union[Person, Organisation]]] = None
    has_source_code: SourceCode = None
