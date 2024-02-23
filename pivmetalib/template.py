import abc
import pathlib
import rdflib
from pydantic import BaseModel, Extra
from typing import Iterable, Union, Dict

from .query_util import query, get_query_string


class _Manager:
    def __init__(self):
        self.data = {}

    def __getitem__(self, cls):
        if cls not in self.data:
            self.data[cls] = {}
        # there might be subclass to this cls. get those data as well
        for k, v in self.data.items():
            if k != cls:
                if issubclass(cls, k):
                    self.data[cls].update(v)
        return self.data[cls]


Context = _Manager()
Namespaces = _Manager()


def namespaces(**kwargs):
    def _decorator(cls):
        for k, v in kwargs.items():
            Namespaces[cls][k] = v
        return cls

    return _decorator


def context(**kwargs):
    def _decorator(cls):
        fields = list(cls.model_fields.keys())
        fields.append(cls.__name__)

        # add fields to the class
        for k, v in kwargs.items():
            if k not in fields:
                raise KeyError(f"Field '{k}' not found in {cls.__name__}")
            Context[cls][k] = v
        return cls

    return _decorator


class AbstractModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Config:
        validate_assignment = True
        extra = Extra.allow

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""

    @property
    def model_iri_fields(self) -> Dict:
        return Context[self.__class__]

    def query(self, source: Union[str, Dict, pathlib.Path]):
        """Return a generator of results from the query."""
        res = query(self.__class__, source)
        if res is None:
            return None

        for r in res:
            if r.id == self.id:
                return r

    def mquery(self,
               sources: Iterable[Union[str, Dict, pathlib.Path]] = None,
               format='json-ld'):
        """Performs query on multiple files or data sources"""
        cls = self.__class__
        mkwargs = [{'source': s, 'format': format} for s in sources]
        query_string = get_query_string(cls)
        bindings = []
        for kwargs in mkwargs:
            g = rdflib.Graph()
            g.parse(**kwargs)

            res = g.query(query_string)
            bindings.extend(res.bindings)

        for binding in bindings:
            if len(binding) > 0:
                yield cls(**{str(k): str(v) for k, v in binding.items() if str(k) != 'id'})
