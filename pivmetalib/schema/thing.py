from pydantic import HttpUrl

import ontolutils
from ontolutils import namespaces, urirefs


@namespaces(schema="https://schema.org/")
@urirefs(Thing='schema:Thing',
         description='schema:description',
         url='schema:url')
class Thing(ontolutils.Thing):
    """schema:Thing (https://schema.org/Thing)
    The most generic type of item."""
    description: str = None
    url: HttpUrl = None
