from pydantic import HttpUrl
from typing import Union, List

from .thing import Thing
from ..prov import Person, Organisation


class CreativeWork(Thing):
    """schema:CreativeWork (not intended to use for modeling)"""
    author: Union[Person, Organisation, List[Union[Person, Organisation]]] = None
    abstract: str = None


class SoftwareApplication(CreativeWork):
    """schema:SoftwareApplication (https://schema.org/SoftwareApplication)"""
    applicationCategory: Union[str, HttpUrl] = None
    downloadURL: HttpUrl = None
    softwareVersion: str = None
    # to be continued


class SoftwareSourceCode(CreativeWork):
    """Pydantic implementation of schema:SoftwareSourceCode (see https://schema.org/SoftwareSourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    codeRepository: HttpUrl
