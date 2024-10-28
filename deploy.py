import json
import pathlib

from pivmetalib import CACHE_DIR
from pivmetalib.utils import download_file

__this_dir__ = pathlib.Path(__file__).parent


def generate_namespace_file():
    """Generate namespace.py file from pivmeta_context.jsonld"""

    namespace = 'pivmeta'

    context_file = CACHE_DIR / 'pivmeta_context.jsonld'
    context_file.unlink(missing_ok=True)  # force download
    if not context_file.exists():
        context_url = "https://raw.githubusercontent.com/matthiasprobst/pivmeta/refs/heads/main/pivmeta_context.jsonld"
        context_file = download_file(context_url, context_file)

    # read context file:
    with open(context_file) as f:
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

    with open(__this_dir__ / 'pivmetalib' / 'namespace.py',
              'w',
              encoding='UTF8') as f:
        f.write('from rdflib.namespace import DefinedNamespace, Namespace\n')
        f.write('from rdflib.term import URIRef\n')
        f.write(f'\n\nclass {namespace.upper()}(DefinedNamespace):')
        f.write('\n    # uri = "https://matthiasprobst.github.io/pivmeta#"')
        f.write('\n    # Generated with pivmetalib')
        for k, v in iris.items():
            f.write(f'\n    {k.replace("-", "_")}: URIRef  # {v["keys"]}')

        f.write(f'\n\n    _NS = Namespace("{url}")')

        f.write('\n\n')

        for k, v in iris.items():
            for kk in v["keys"]:
                key = kk.replace(' ', '_')
                f.write(f'\nsetattr({namespace.upper()}, "{key}", {namespace.upper()}.{k.replace("-", "_")})')


if __name__ == '__main__':
    generate_namespace_file()
