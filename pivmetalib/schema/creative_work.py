from typing import Union, List

from pydantic import HttpUrl
from pydantic import field_validator

from ontolutils import Thing, namespaces, urirefs


@namespaces(schema="https://schema.org/")
@urirefs(Organization='schema:Organization',
         name='schema:name')
class Organization(Thing):
    """schema:Organization (https://schema.org/Organization)"""
    name: str = None


@namespaces(schema="https://schema.org/")
@urirefs(Person='schema:Person',
         given_name='schema:givenName',
         family_name='schema:familyName',
         email='schema:email',
         affiliation='schema:affiliation'
         )
class Person(Thing):
    """schema:Person (https://schema.org/Person)"""
    given_name: str = None
    family_name: str = None
    email: str = None
    affiliation: Union[Organization, List[Organization]] = None


@namespaces(schema="https://schema.org/")
@urirefs(CreativeWork='schema:CreativeWork',
         author='schema:author',
         abstract='schema:abstract')
class CreativeWork(Thing):
    """schema:CreativeWork (not intended to use for modeling)"""
    author: Union[Person, Organization, List[Union[Person, Organization]]] = None
    abstract: str = None


@namespaces(schema="https://schema.org/")
@urirefs(SoftwareApplication='schema:SoftwareApplication',
         application_category='schema:applicationCategory',
         download_URL='schema:downloadURL',
         software_version='schema:softwareVersion')
class SoftwareApplication(CreativeWork):
    """schema:SoftwareApplication (https://schema.org/SoftwareApplication)"""
    application_category: Union[str, HttpUrl] = None
    download_URL: HttpUrl = None
    software_version: str = None

    @field_validator('application_category')
    @classmethod
    def _validate_applicationCategory(cls, application_category: Union[str, HttpUrl]):
        if application_category.startswith('file:'):
            return application_category.rsplit('/', 1)[-1]
        return application_category


@namespaces(schema="https://schema.org/")
@urirefs(SoftwareSourceCode='schema:SoftwareSourceCode',
         code_repository='schema:codeRepository',
         application_category='schema:applicationCategory')
class SoftwareSourceCode(CreativeWork):
    """Pydantic implementation of schema:SoftwareSourceCode (see https://schema.org/SoftwareSourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    code_repository: Union[HttpUrl, str] = None
    application_category: Union[str, HttpUrl] = None

    @field_validator('code_repository')
    @classmethod
    def _validate_code_repository(cls, code_repository: Union[str, HttpUrl]):
        if not isinstance(code_repository, str):
            return code_repository
        if code_repository.startswith('git+'):
            _url = HttpUrl(code_repository.split("git+", 1)[1])
            # return f'{_url}'
        return code_repository

    @field_validator('application_category')
    @classmethod
    def _validate_applicationCategory(cls, application_category: Union[str, HttpUrl]):
        if application_category.startswith('file:'):
            return application_category.rsplit('/', 1)[-1]
        return application_category
