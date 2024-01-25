import abc
from pydantic import BaseModel


class AbstractModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Config:
        validate_assignment = True

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
