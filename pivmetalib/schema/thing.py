import ontolutils
from pydantic import HttpUrl

from ontolutils import Thing, namespaces, urirefs


@namespaces(schema="https://schema.org/")
@urirefs(Thing='schema:Thing',
         description='schema:description',
         url='schema:url')
class Thing(ontolutils.Thing):
    """schema:Thing (https://schema.org/Thing)
    The most generic type of item."""
    description: str = None
    url: HttpUrl = None
