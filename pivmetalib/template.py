import abc
import pathlib
import rdflib
from pydantic import BaseModel
from typing import Iterable, Union, Dict


def namespaces(**kwargs):
    def _decorator(cls):
        for k, v in kwargs.items():
            cls.Namespaces.namespaces[k] = v
        return cls

    return _decorator


def context(**kwargs):
    def _decorator(cls):
        fields = list(cls.model_fields.keys())
        fields.append(cls.__name__)
        for k, v in kwargs.items():
            if k not in fields:
                raise KeyError(f"Field '{k}' not found in {cls.__name__}")
            cls.Context.namespace[k] = v
        return cls

    return _decorator


def get_query_string(cls) -> str:
    def _get_namespace(key):
        ns = cls.Context.namespace.get(key, f'local:{key}')
        if ':' in ns:
            return ns
        return f'{ns}:{key}'

    # generate query automatically based on fields
    fields = " ".join([f"?{k}" for k in cls.model_fields.keys()])
    # better in a one-liner:
    query_str = "".join([f"PREFIX {k}: <{v}>\n" for k, v in cls.Namespaces.namespaces.items()])

    query_str += f"""
SELECT ?id {fields}
WHERE {{{{
    ?id a {_get_namespace(cls.__name__)} ."""

    for field in cls.model_fields.keys():
        if cls.model_fields[field].is_required():
            query_str += f"\n    ?id {_get_namespace(field)} ?{field} ."
        else:
            query_str += f"\n    OPTIONAL {{ ?id {_get_namespace(field)} ?{field} . }}"
    query_str += "\n}}"
    return query_str


def query(cls, *args, **kwargs):
    query_string = get_query_string(cls)
    g = rdflib.Graph()
    g.parse(*args, **kwargs)

    res = g.query(query_string)
    for binding in res.bindings:
        yield cls(**{str(k): str(v) for k, v in binding.items() if str(k) != 'id'})


class AbstractModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Namespaces:
        namespaces = {}

    class Context:
        namespace = {}

    class Config:
        validate_assignment = True

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""

    @classmethod
    def query(cls, *args, **kwargs):
        """Return a generator of results from the query."""
        return query(cls, *args, **kwargs)

    @classmethod
    def mquery(cls,
               sources: Iterable[Union[str, Dict, pathlib.Path]] = None,
               format='json-ld'):
        """Performs query on multiple files or data sources"""
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

    @classmethod
    def mquery_one(cls,
                   sources: Iterable[Union[str, Dict, pathlib.Path]] = None,
                   format='json-ld'):
        """Return the first result of the query, or None if no results are found."""
        for r in cls.mquery(cls, sources, format):
            return r

    @classmethod
    def query_one(cls, *args, **kwargs):
        """Return the first result of the query, or None if no results are found."""
        for r in cls.query(cls, *args, **kwargs):
            return r
