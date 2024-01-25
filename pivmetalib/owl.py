import json
import rdflib
from datetime import datetime
from typing import Dict

from .template import AbstractModel


def serialize_fields(obj, exclude_none: bool = True) -> Dict:
    """Serializes the fields of a Thing object into a json-ld dictionary (without context!)"""
    if exclude_none:
        serialized_fields = {k: getattr(obj, k) for k in obj.model_fields if getattr(obj, k) is not None}
    else:
        serialized_fields = {k: getattr(obj, k) for k in obj.model_fields}

    # datetime
    for k, v in serialized_fields.copy().items():
        if isinstance(v, datetime):
            # field_dict[k] = v.strftime('%Y-%m-%d')
            serialized_fields[k] = v.isoformat()
        elif isinstance(v, Thing):
            serialized_fields[k] = serialize_fields(v, exclude_none=exclude_none)
        elif isinstance(v, list):
            serialized_fields[k] = [serialize_fields(i, exclude_none=exclude_none) for i in v]
        else:
            serialized_fields[k] = str(v)
    return {"@type": f"ssno:{obj.__class__.__name__}", **serialized_fields}


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


class Thing(AbstractModel):
    """owl:Thing
    """
    name: str = None

    def dump_jsonld(self, id=None, context=None, exclude_none: bool = True) -> str:
        """alias for model_dump_json()"""
        if context is None:
            from . import CONTEXT
            context = CONTEXT

        g = rdflib.Graph()
        _atemp_json_dict = serialize_fields(self, exclude_none=exclude_none)

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

    def __repr__(self):
        _fields = {k: getattr(self, k) for k in self.model_fields if getattr(self, k) is not None}
        repr_fields = ", ".join([f"{k}={v}" for k, v in _fields.items()])
        return f"{self.__class__.__name__}({repr_fields})"

    def _repr_html_(self) -> str:
        """Returns the HTML representation of the class"""
        _fields = {k: getattr(self, k) for k in self.model_fields if getattr(self, k) is not None}
        repr_fields = ", ".join([f"{k}={v}" for k, v in _fields.items()])
        return f"{self.__class__.__name__}({repr_fields})"
