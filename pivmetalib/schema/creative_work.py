from typing import Union, List

from pydantic import HttpUrl
from pydantic import field_validator

from ontolutils import Thing, namespaces, urirefs


@namespaces(schema="http://schema.org/")
@urirefs(Organization='schema:Organization',
         name='schema:name')
class Organization(Thing):
    """schema:Organization (http://schema.org/Organization)"""
    name: str = None


@namespaces(schema="http://schema.org/")
@urirefs(Person='schema:Person',
         givenName='schema:givenName',
         familyName='schema:familyName',
         email='schema:email',
         affiliation='schema:affiliation'
         )
class Person(Thing):
    """schema:Person (http://schema.org/Person)"""
    givenName: str = None
    familyName: str = None
    email: str = None
    affiliation: Union[Organization, List[Organization]] = None


@namespaces(schema="http://schema.org/")
@urirefs(CreativeWork='schema:CreativeWork',
         author='schema:author',
         abstract='schema:abstract')
class CreativeWork(Thing):
    """schema:CreativeWork (not intended to use for modeling)"""
    author: Union[Person, Organization, List[Union[Person, Organization]]] = None
    abstract: str = None


@namespaces(schema="http://schema.org/")
@urirefs(SoftwareApplication='schema:SoftwareApplication',
         applicationCategory='schema:applicationCategory',
         downloadURL='schema:downloadURL',
         softwareVersion='schema:softwareVersion')
class SoftwareApplication(CreativeWork):
    """schema:SoftwareApplication (http://schema.org/SoftwareApplication)"""
    applicationCategory: Union[str, HttpUrl] = None
    downloadURL: HttpUrl = None
    softwareVersion: str = None

    @field_validator('applicationCategory')
    @classmethod
    def _validate_applicationCategory(cls, applicationCategory: Union[str, HttpUrl]):
        if applicationCategory.startswith('file:'):
            return applicationCategory.rsplit('/', 1)[-1]
        return applicationCategory

    # to be continued


@namespaces(schema="http://schema.org/")
@urirefs(SoftwareSourceCode='schema:SoftwareSourceCode',
         codeRepository='schema:codeRepository',
         applicationCategory='schema:applicationCategory')
class SoftwareSourceCode(CreativeWork):
    """Pydantic implementation of schema:SoftwareSourceCode (see http://schema.org/SoftwareSourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    codeRepository: Union[HttpUrl, str] = None
    applicationCategory: Union[str, HttpUrl] = None

    @field_validator('codeRepository')
    @classmethod
    def _validate_codeRepository(cls, codeRepository: Union[str, HttpUrl]):
        if not isinstance(codeRepository, str):
            return codeRepository
        if codeRepository.startswith('git+'):
            _url = HttpUrl(codeRepository.split("git+", 1)[1])
            # return f'{_url}'
        return codeRepository

    @field_validator('applicationCategory')
    @classmethod
    def _validate_applicationCategory(cls, applicationCategory: Union[str, HttpUrl]):
        if applicationCategory.startswith('file:'):
            return applicationCategory.rsplit('/', 1)[-1]
        return applicationCategory
