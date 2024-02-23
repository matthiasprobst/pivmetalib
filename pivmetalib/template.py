import abc
import pathlib
import rdflib
from pydantic import BaseModel, Extra
from typing import Iterable, Union, Dict

from .query_util import query, get_query_string


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


#         res_str_dict['_id'] = res_str_dict.pop('id', None)
#         # now check if any of the values is an ID within the graph
#         # for this, first get all IDs:
#         ids_query = """
# SELECT DISTINCT ?id
# WHERE {
#   ?id a ?class
# }
# """
#         ids = {str(_id): _id.n3() for _id, in g.query(ids_query)}
#         for k, _id in res_str_dict.items():
#             if _id in ids.keys():
#                 # get the class of the ID
#                 class_query = f"""
# SELECT ?class
# WHERE {{
#     ?id a {ids[_id]}
# }}
# """
#                 class_res = g.query(class_query)
#                 # res_str_dict[k] = {str(_class) for _class

# yield cls.parse_jsonld(res_str_dict)
# yield cls(**res_str_dict)


class AbstractModel(abc.ABC, BaseModel):
    """Abstract class to be used by model classes used within PIVMetalib"""

    class Namespaces:
        namespaces = {}

    class Context:
        namespace = {}

    class Config:
        validate_assignment = True
        extra = Extra.allow

    @abc.abstractmethod
    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""

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
