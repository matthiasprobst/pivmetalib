import abc
from pydantic import BaseModel


class AbstractModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Config:
        validate_assignment = True

    def __repr__(self):
        """Returns the representation of the class, which is all none-None fields"""
        fields = ", ".join([f"{k}={v}" for k, v in self.model_dump(exclude_none=True).items()])
        return f"{self.__class__.__name__}({fields})"

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
