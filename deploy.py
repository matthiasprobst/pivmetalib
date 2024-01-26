import json
import pathlib

from pivmetalib import CACHE_DIR, CONTEXT
from pivmetalib.utils import download_file

__this_dir__ = pathlib.Path(__file__).parent


def generate_namespace_file(namespace, context):
    """Generate <namespace>.py file from context jsonld file"""

    context_file = CACHE_DIR / f'{namespace}_context.jsonld'
    context_file.unlink(missing_ok=True)  # force download
    if not context_file.exists():
        context_file = download_file(context, context_file)

    # read context file:
    with open(context_file, encoding='utf-8') as f:
        context = json.load(f)

    url = context['@context'][namespace]

    iris = {}
    for k, v in context['@context'].items():
        if '@id' in v:
            if namespace in v['@id']:
                name = v["@id"].rsplit(":", 1)[-1]
                if name not in iris:
                    iris[name] = {'url': f'{url}{name}', 'keys': [k, ]}
                else:
                    iris[name]['keys'].append(k)
            else:
                print(f'Skipping {k}={v} because it is not in the "{namespace}" namespace')

    namespace_py_filename = __this_dir__ / 'pivmetalib/namespace' / f'{namespace}.py'
    with open(namespace_py_filename, 'w', encoding='UTF8') as f:
        f.write('from rdflib.namespace import DefinedNamespace, Namespace\n')
        f.write('from rdflib.term import URIRef\n')
        f.write(f'\n\nclass {namespace.upper()}(DefinedNamespace):')
        f.write('\n    # uri = "https://w3id.org/nfdi4ing/metadata4ing#"')
        f.write('\n    # Generated with h5rdmtoolbox.data.m4i.generate_namespace_file()')
        for k, v in iris.items():
            f.write(f'\n    {k}: URIRef  # {v["keys"]}')

        f.write(f'\n\n    _NS = Namespace("{url}")')

        f.write('\n\n')

        for k, v in iris.items():
            for kk in v["keys"]:
                key = kk.replace(' ', '_')
                f.write(f'\nsetattr({namespace.upper()}, "{key}", {namespace.upper()}.{k})')
    return namespace_py_filename.stem, namespace.upper()


if __name__ == '__main__':
    with open(__this_dir__ / 'pivmetalib/namespace/__init__.py', 'w') as f:
        fname, name = generate_namespace_file(
            'pivmeta',
            context=CONTEXT
        )
        f.write(f'from .{fname} import {name}\n')
        fname, name = generate_namespace_file(
            'ssno',
            context='https://raw.githubusercontent.com/matthiasprobst/ssno/main/ssno_context.jsonld'
        )
        f.write(f'from .{fname} import {name}\n')

