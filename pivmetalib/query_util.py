import pathlib
import rdflib
from typing import Union, Dict, List


def get_query_string(cls) -> str:
    def _get_namespace(key):
        ns = cls.Context.namespace.get(key, f'local:{key}')
        if ':' in ns:
            return ns
        return f'{ns}:{key}'

    # generate query automatically based on fields
    fields = " ".join([f"?{k}" for k in cls.model_fields.keys() if k != 'id'])
    # better in a one-liner:
    query_str = "".join([f"PREFIX {k}: <{v}>\n" for k, v in cls.Namespaces.namespaces.items()])

    query_str += f"""
SELECT ?id {fields}
WHERE {{{{
    ?id a {_get_namespace(cls.__name__)} ."""

    for field in cls.model_fields.keys():
        if field != 'id':
            if cls.model_fields[field].is_required():
                query_str += f"\n    ?id {_get_namespace(field)} ?{field} ."
            else:
                query_str += f"\n    OPTIONAL {{ ?id {_get_namespace(field)} ?{field} . }}"
    query_str += "\n}}"
    return query_str


def get_query_string(cls) -> str:
    def _get_namespace(key):
        ns = cls.Context.namespace.get(key, f'local:{key}')
        if ':' in ns:
            return ns
        return f'{ns}:{key}'

    # generate query automatically based on fields
    # fields = " ".join([f"?{k}" for k in cls.model_fields.keys() if k != 'id'])
    # better in a one-liner:
    # query_str = "".join([f"PREFIX {k}: <{v}>\n" for k, v in cls.Namespaces.namespaces.items()])

    query_str = f"""
SELECT *
WHERE {{{{
    ?id a {_get_namespace(cls.__name__)} .
    ?id ?p ?o ."""

    # for field in cls.model_fields.keys():
    #     if field != 'id':
    #         if cls.model_fields[field].is_required():
    #             query_str += f"\n    ?id {_get_namespace(field)} ?{field} ."
    #         else:
    #             query_str += f"\n    OPTIONAL {{ ?id {_get_namespace(field)} ?{field} . }}"
    query_str += "\n}}"
    return query_str


class QueryResult:

    def __init__(self, cls, source: Union[str, Dict, pathlib.Path], n3dict):
        self.cls = cls
        self.source = source  # Dict or json-ld file!
        for k, v in n3dict.items():
            assert k.startswith('?')
            if v.startswith('<') and k != '?id':
                # it is a URIRef
                mfield = cls.model_fields[k[1:]]
                from .owl import Thing
                if isinstance(mfield, Thing):
                    # it is a Thing
                    setattr(self, k[1:], mfield.cls(id=v[1:-1]))
                else:
                    flag = False
                    for arg in mfield.annotation.__args__:
                        if issubclass(arg, Thing):
                            # it is a Thing
                            setattr(self, k[1:], arg(id=v[1:-1]))
                            flag = True
                            break
                    if not flag:
                        setattr(self, k[1:], v[1:-1])
            else:
                setattr(self, k[1:], v[1:-1])

    def __repr__(self):
        return f"{self.__class__.__name__}(cls={self.cls.__name__})"

    def parse(self):
        return self.cls.parse_obj(self.dict())


def _get_class_from_model_field(field):
    # guess the object
    from .owl import Thing
    try:
        annotation_args = field.annotation.__args__
    except AttributeError:
        return field.annotation

    if isinstance(annotation_args, tuple):
        # one of the args must be a Thing!!!
        for arg in annotation_args:
            if issubclass(arg, Thing):
                # it is a Thing
                return arg
                # return arg(id=o)
    else:
        return annotation_args


def query(cls, source: Union[str, Dict, pathlib.Path]) -> List:
    """Return a generator of results from the query."""

    query_string = get_query_string(cls)
    g = rdflib.Graph()

    for k, p in cls.Namespaces.namespaces.items():
        g.bind(k, p)

    g.parse(source=source, format='json-ld',
            context="https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld")

    res = g.query(query_string)

    if len(res) == 0:
        return None

    # get model field dict as IRI
    # e.g. {'http://www.w3.org/2000/01/rdf-schema#description': 'description'}
    model_field_iri = {}
    for model_field, iri in cls.Context.namespace.items():
        ns, key = iri.split(':', 1)
        ns_iri = cls.Namespaces.namespaces.get(ns, None)
        if ns_iri is None:
            full_iri = key
        else:
            full_iri = f'{cls.Namespaces.namespaces.get(ns)}{key}'
        model_field_iri[full_iri] = model_field

    n3dict = {}
    for binding in res.bindings:
        _id = binding['?id'].n3()
        if _id not in n3dict:
            n3dict[_id] = {}
        p = binding['?p'].__str__()
        _o = binding['?o'].n3()
        if _o.startswith('<'):
            # it is a URIRef
            o = _o[1:-1]

            # now there are two cases:
            # 1. the predicate belonging to the object is defined in the model
            # 2. the predicate belonging to the object is NOT defined in the model. then we just pass the string
            # So with have to act only on case 1
            model_field = model_field_iri.get(p, None)
            if model_field is None:
                pass
            else:
                _fieldcls = _get_class_from_model_field(field=cls.model_fields[model_field])
                o = _fieldcls(id=o)
        else:
            o = _o[1:-1]
        if p in n3dict[_id]:
            if isinstance(n3dict[_id][p], list):
                n3dict[_id][p].append(o)
            else:
                n3dict[_id][p] = [n3dict[_id][p], o]
        else:
            n3dict[_id][p] = o

    results = []
    for _id, _params in n3dict.items():
        kwargs = {}
        # translate IRI to model field
        for k, v in _params.items():
            if ':' in k:
                _abbr, _model_field_name = k.split(':', 1)
                if _abbr in cls.Namespaces.namespaces:
                    model_field = cls.model_fields.get(_model_field_name, None)
                    if model_field is None:
                        _key = _model_field_name
                    else:
                        model_cls = _get_class_from_model_field(field=model_field)
                        kwargs[_model_field_name] = model_cls(id=v)
                        continue
            _key = model_field_iri.get(k, None)
            if _key is None:
                # The IRI is not defined in the model.
                if '#' in k:
                    _base_uri, _key = k.split('#', 1)
                else:
                    _base_uri, _key = k.rsplit('/', 1)
            if _key != 'type':
                kwargs[_key] = v
        results.append(cls(id=_id[1:-1], **kwargs))
    return results
    #     resuts.append(cls(id=_id, **kwargs))
    # for r in resuts:
    #     yield r

    # for binding in res.bindings:
    #     # Issue: A value of a field may be a URIRef, e.g. a Distribution within a Dataset
    #     # The easy solution is, that hasDistribution allows strings as well...
    #     # The less easy solution is to call a query, which gets all entries for the distribution
    #     # Let's do the latter:
    #     n3dict = {k.n3(): v.n3() for k, v in binding.items()}
    #
    #     cls_data = {}
    #
    #     for k, v in n3dict.items():
    #         assert k.startswith('?')
    #         if v.startswith('<') and k != '?id':
    #             # it is a URIRef
    #             mfield = cls.model_fields[k[1:]]
    #             from .owl import Thing
    #             if isinstance(mfield, Thing):
    #                 # it is a Thing
    #                 cls_data[k[1:]] = mfield.cls(id=v[1:-1])
    #                 # setattr(self, k[1:], mfield.cls(id=v[1:-1]))
    #             else:
    #                 flag = False
    #                 for arg in mfield.annotation.__args__:
    #                     if issubclass(arg, Thing):
    #                         # it is a Thing
    #                         cls_data[k[1:]] = arg(id=v[1:-1])
    #                         # setattr(self, k[1:], arg(id=v[1:-1]))
    #                         flag = True
    #                         break
    #                 if not flag:
    #                     cls_data[k[1:]] = v[1:-1]
    #                     # setattr(self, k[1:], v[1:-1])
    #         else:
    #             cls_data[k[1:]] = v[1:-1]
    #             # setattr(self, k[1:], v[1:-1])
    #     yield cls.parse_obj(cls_data)
    #
    #     # yield QueryResult(cls, source, n3dict)
    #
    #     """If the object is a blank node the following will fail, so always use a local namespace"""
    #
    #     # res_str_dict = {k.n3(): v.n3() for k, v in binding.items()}
