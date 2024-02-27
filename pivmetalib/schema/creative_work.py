from pydantic import HttpUrl
from typing import Union, List

from .thing import Thing
from ..prov import Person, Organisation
from ..model import namespaces, context


@namespaces(schema="https://schema.org/")
@context(CreativeWork='schema:CreativeWork',
         author='schema:author',
         abstract='schema:abstract')
class CreativeWork(Thing):
    """schema:CreativeWork (not intended to use for modeling)"""
    author: Union[Person, Organisation, List[Union[Person, Organisation]]] = None
    abstract: str = None


@context(SoftwareApplication='schema:SoftwareApplication',
         applicationCategory='schema:applicationCategory',
         downloadURL='schema:downloadURL',
         softwareVersion='schema:softwareVersion')
class SoftwareApplication(CreativeWork):
    """schema:SoftwareApplication (https://schema.org/SoftwareApplication)"""
    applicationCategory: Union[str, HttpUrl] = None
    downloadURL: HttpUrl = None
    softwareVersion: str = None
    # to be continued


@context(SoftwareSourceCode='schema:SoftwareSourceCode',
         codeRepository='schema:codeRepository')
class SoftwareSourceCode(CreativeWork):
    """Pydantic implementation of schema:SoftwareSourceCode (see https://schema.org/SoftwareSourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    codeRepository: HttpUrl
