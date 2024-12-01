from typing import Union, List

from pydantic import HttpUrl
from pydantic import field_validator, Field

from ontolutils import Thing, namespaces, urirefs


@namespaces(schema="https://schema.org/")
@urirefs(Organization='schema:Organization',
         name='schema:name')
class Organization(Thing):
    """schema:Organization (https://schema.org/Organization)"""
    name: str = None


@namespaces(schema="https://schema.org/")
@urirefs(Person='schema:Person',
         givenName='schema:givenName',
         familyName='schema:familyName',
         email='schema:email',
         affiliation='schema:affiliation'
         )
class Person(Thing):
    """schema:Person (https://schema.org/Person)"""
    givenName: str = Field(alias="given_name")
    familyName: str = Field(alias="family_name", default=None)
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
         applicationCategory='schema:applicationCategory',
         downloadURL='schema:downloadURL',
         version='schema:softwareVersion')
class SoftwareApplication(CreativeWork):
    """schema:SoftwareApplication (https://schema.org/SoftwareApplication)"""
    applicationCategory: Union[str, HttpUrl] = Field(default=None, alias="application_category")
    downloadURL: HttpUrl = Field(default=None, alias="download_URL")
    version: str = Field(default=None, alias="softwareVersion")

    @field_validator('applicationCategory')
    @classmethod
    def _validate_applicationCategory(cls, application_category: Union[str, HttpUrl]):
        if application_category.startswith('file:'):
            return application_category.rsplit('/', 1)[-1]
        return application_category


@namespaces(schema="https://schema.org/")
@urirefs(SoftwareSourceCode='schema:SoftwareSourceCode',
         codeRepository='schema:codeRepository',
         applicationCategory='schema:applicationCategory')
class SoftwareSourceCode(CreativeWork):
    """Pydantic implementation of schema:SoftwareSourceCode (see https://schema.org/SoftwareSourceCode)

    .. note::

        More than the below parameters are possible but not explicitly defined here.
    """
    codeRepository: Union[HttpUrl, str] = Field(default=None, alias="code_repository")
    applicationCategory: Union[str, HttpUrl] = Field(default=None, alias="application_category")

    @field_validator('codeRepository')
    @classmethod
    def _validate_code_repository(cls, code_repository: Union[str, HttpUrl]):
        if not isinstance(code_repository, str):
            return code_repository
        if code_repository.startswith('git+'):
            _url = HttpUrl(code_repository.split("git+", 1)[1])
            # return f'{_url}'
        return code_repository

    @field_validator('applicationCategory')
    @classmethod
    def _validate_applicationCategory(cls, application_category: Union[str, HttpUrl]):
        if application_category.startswith('file:'):
            return application_category.rsplit('/', 1)[-1]
        return application_category
