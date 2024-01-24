from pydantic import HttpUrl

from .. import owl


class Thing(owl.Thing):
    """schema:Thing (https://schema.org/Thing)
    The most generic type of item."""
    name: str = None
    description: str = None
    url: HttpUrl = None
