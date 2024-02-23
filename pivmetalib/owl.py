import json
import rdflib
import uuid
from datetime import datetime
from pydantic import HttpUrl, FileUrl
from typing import Dict, Union

from .template import AbstractModel, context, namespaces, Context


# def serialize(obj):
#     data = {Context[obj.__class__][k]: getattr(obj, k) for k in obj.model_fields if
#      getattr(obj, k) is not None}
#
#     for k, v in data.copy().items():
#         if isinstance(v, datetime):
#             data[k] = v.isoformat()
#         elif isinstance(v, dict):
#             return serialize(v)
#         elif isinstance(v, list):
#             for i in v:
#                 if isinstance(i, dict):
#                     return serialize(i)
#         elif isinstance(v, AbstractModel):
#             data[k] = serialize(v)
#     return data


def serialize_fields(obj, exclude_none: bool = True, prefix: str = None) -> Dict:
    """Serializes the fields of a Thing object into a json-ld dictionary (without context!)"""

    if exclude_none:
        serialized_fields = {Context[obj.__class__][k]: getattr(obj, k) for k in obj.model_fields if
                             getattr(obj, k) is not None}
        # serialized_fields = {_parse_key(k): getattr(obj, k) for k in obj.model_fields if getattr(obj, k) is not None}
    else:
        serialized_fields = {Context[obj.__class__][k]: getattr(obj, k) for k in obj.model_fields}
        # serialized_fields = {_parse_key(k): getattr(obj, k) for k in obj.model_fields}
    for k, v in obj.model_extra.items():
        serialized_fields[Context[obj.__class__].get(k, k)] = v

    # datetime
    for k, v in serialized_fields.copy().items():
        _field = serialized_fields.pop(k)
        # if hasattr(v, '_KEY_PREFIX'):
        #     key = f"{v._KEY_PREFIX}:{k}"
        # else:
        #     key = k
        key = k
        if isinstance(v, datetime):
            # field_dict[k] = v.strftime('%Y-%m-%d')
            serialized_fields[key] = v.isoformat()
        elif isinstance(v, Thing):
            serialized_fields[key] = serialize_fields(v, exclude_none=exclude_none)
        elif isinstance(v, list):
            serialized_fields[key] = [serialize_fields(i, exclude_none=exclude_none) for i in v]
        else:
            serialized_fields[key] = str(v)

    _type = Context[obj.__class__].get(obj.__class__.__name__, obj.__class__.__name__)

    return {"@type": _type, **serialized_fields,
            "@id": obj.id if obj.id is not None else f'local:{str(uuid.uuid4())}'}


def _repr(obj):
    if hasattr(obj, '_repr_html_'):
        return obj._repr_html_()
    if isinstance(obj, list):
        return f"[{', '.join([_repr(i) for i in obj])}]"
    if isinstance(obj, rdflib.URIRef):
        return str(obj)
    return repr(obj)


def _html_repr(obj):
    if hasattr(obj, '_repr_html_'):
        return obj._repr_html_()
    if isinstance(obj, list):
        return f"[{', '.join([_repr(i) for i in obj])}]"
    if isinstance(obj, rdflib.URIRef):
        return f"<a href='{obj}'>{obj}</a>"
    return repr(obj)


def dump_hdf(g, data: Dict):
    """Write a dictionary to a hdf group. Nested dictionaries result in nested groups"""
    for k, v in data.items():
        if isinstance(v, dict):
            sub_g = g.create_group(k)
            dump_hdf(sub_g, v)
        else:
            g.attrs[k] = v


@namespaces(owl='http://www.w3.org/2002/07/owl#',
            rdfs='http://www.w3.org/2000/01/rdf-schema#',
            local='http://example.com/')
@context(Thing='owl:Thing', label='rdfs:label')
class Thing(AbstractModel):
    """owl:Thing
    """
    id: Union[str, HttpUrl, FileUrl, None] = None  # @id
    label: str = None  # rdfs:label
    None

    def dump_jsonld(self, context=None, exclude_none: bool = True,
                    local_namespace: HttpUrl = 'https://local-domain.org/') -> str:
        """alias for model_dump_json()"""

        if context is None:
            from . import CONTEXT
            context = CONTEXT

        g = rdflib.Graph()

        at_context: Dict = {"@import": context,
                            "local": local_namespace}
        jsonld = {
            "@context": at_context,
            "@graph": [
                serialize_fields(self)
            ]
        }

        g.parse(data=json.dumps(jsonld), format='json-ld')
        if context:
            return g.serialize(format='json-ld',
                               context={"@import": context},
                               indent=4)
        return g.serialize(format='json-ld', indent=4)

    def dump_hdf(self, g, name: str = None):
        """Write the object to an hdf group. Nested dictionaries result in nested groups"""
        if name is None:
            name = self.__class__.__name__
        dump_hdf(g, {name: self.model_dump(exclude_none=True)})

    def __repr__(self):
        _fields = {k: getattr(self, k) for k in self.model_fields if getattr(self, k) is not None}
        repr_fields = ", ".join([f"{k}={v}" for k, v in _fields.items()])
        repr_extra = ", ".join([f"{k}={v}" for k, v in self.model_extra.items()])
        return f"{self.__class__.__name__}({repr_fields}, {repr_extra})"

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        _fields = {k: getattr(self, k) for k in self.model_fields if getattr(self, k) is not None}
        repr_fields = ", ".join([f"{k}={v}" for k, v in _fields.items()])
        return f"{self.__class__.__name__}({repr_fields})"
