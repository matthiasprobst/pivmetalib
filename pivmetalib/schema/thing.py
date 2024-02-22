from pydantic import HttpUrl

from .. import owl
from ..template import namespaces, context


@namespaces(schema="https://schema.org/")
@context(Thing='schema:Thing',
         description='schema:description',
         url='schema:url')
class Thing(owl.Thing):
    """schema:Thing (https://schema.org/Thing)
    The most generic type of item."""
    description: str = None
    url: HttpUrl = None
    _PREFIX = 'schema'
