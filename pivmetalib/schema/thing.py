from pydantic import HttpUrl

from .. import owl
from .. import namespaces, urirefs


@namespaces(schema="https://schema.org/")
@urirefs(Thing='schema:Thing',
         description='schema:description',
         url='schema:url')
class Thing(owl.Thing):
    """schema:Thing (https://schema.org/Thing)
    The most generic type of item."""
    description: str = None
    url: HttpUrl = None
