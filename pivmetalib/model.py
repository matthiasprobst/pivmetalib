import abc
import pathlib
import rdflib
from pydantic import BaseModel, Extra
from typing import Iterable, Union, Dict


class PivMetaBaseModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Config:
        validate_assignment = True
        # extra = Extra.forbid
        extra = Extra.allow

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""

    # def query(self, source: Union[str, Dict, pathlib.Path]):
    #     """Return a generator of results from the query."""
    #     from .query_util import query
    #     res = query(self.__class__, source)
    #     if res is None:
    #         return None
    #
    #     for r in res:
    #         if r.id == self.id:
    #             return r
    #
    # def mquery(self,
    #            sources: Iterable[Union[str, Dict, pathlib.Path]] = None,
    #            format='json-ld'):
    #     """Performs query on multiple files or data sources"""
    #     from .query_util import get_query_string
    #     cls = self.__class__
    #     mkwargs = [{'source': s, 'format': format} for s in sources]
    #     query_string = get_query_string(cls)
    #     bindings = []
    #     for kwargs in mkwargs:
    #         g = rdflib.Graph()
    #         g.parse(**kwargs)
    #
    #         res = g.query(query_string)
    #         bindings.extend(res.bindings)
    #
    #     for binding in bindings:
    #         if len(binding) > 0:
    #             yield cls(**{str(k): str(v) for k, v in binding.items() if str(k) != 'id'})
