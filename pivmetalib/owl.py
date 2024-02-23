import json
import rdflib
from datetime import datetime
from pydantic import HttpUrl, FileUrl, Field
from typing import Dict, Union

from .template import AbstractModel, context, namespaces


def serialize_fields(obj, exclude_none: bool = True, prefix: str = None) -> Dict:
    """Serializes the fields of a Thing object into a json-ld dictionary (without context!)"""

    def _parse_key(_key):
        return _key.replace('_', ' ')

    if exclude_none:
        serialized_fields = {_parse_key(k): getattr(obj, k) for k in obj.model_fields if getattr(obj, k) is not None}
    else:
        serialized_fields = {_parse_key(k): getattr(obj, k) for k in obj.model_fields}

    # datetime
    for k, v in serialized_fields.copy().items():
        _field = serialized_fields.pop(k)
        if hasattr(v, '_KEY_PREFIX'):
            key = f"{v._KEY_PREFIX}:{k}"
        else:
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
    if prefix is not None:
        _type = f"{prefix}:{obj.__class__.__name__}"
    else:
        _type = f"{obj.__class__.__name__}"
    return {"@type": _type, **serialized_fields}


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

from pydantic import Field
@namespaces(owl='http://www.w3.org/2002/07/owl#',
            rdfs='http://www.w3.org/2000/01/rdf-schema#',
            local='http://example.com/')
@context(Thing='owl:Thing', label='rdfs:label')
class Thing(AbstractModel):
    """owl:Thing
    """
    id: Union[str, HttpUrl, FileUrl, None] # @id
    label: str = None  # rdfs:label
    _PREFIX = None

    def dump_jsonld(self, id=None, context=None, exclude_none: bool = True) -> str:
        """alias for model_dump_json()"""

        if context is None:
            from . import CONTEXT
            context = CONTEXT

        g = rdflib.Graph()
        _atemp_json_dict = serialize_fields(
            self,
            exclude_none=exclude_none,
            prefix=self._PREFIX
        )

        if id is None:
            _id = '_:'
        else:
            _id = id
        jsonld = {"@context": {"@import": context},
                  "@graph": [
                      {"@id": _id,
                       **_atemp_json_dict}
                  ]}

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
