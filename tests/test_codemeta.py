import json
import pathlib

import pivmetalib
import utils
from ontolutils.classes.utils import download_file
from pivmetalib import __version__
from pivmetalib.schema import SoftwareSourceCode

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestCodemeta(utils.ClassTest):

    def test_codemeta(self):
        # get codemeta context file:
        codemeta_context_file = download_file(
            'https://raw.githubusercontent.com/codemeta/codemeta/2.0/codemeta.jsonld',
            None)
        with open(codemeta_context_file) as f:
            codemeta_context = json.load(f)['@context']

        codemeta_filename = __this_dir__ / '../codemeta.json'
        with open(codemeta_filename, encoding='utf-8') as f:
            data = json.load(f)
            # ssc = SoftwareSourceCode.from_jsonld(data=data)

        # replace context in data
        _ = data.pop('@context')
        data['@context'] = codemeta_context

        ssc = SoftwareSourceCode.from_jsonld(data=json.dumps(data), limit=1)
        self.assertEqual(ssc.name, 'pivmetalib')
        self.assertEqual(ssc.code_repository, "git+https://github.com/matthiasprobst/pivmetalib")
        self.assertEqual(ssc.version, __version__)
        self.assertEqual(len(ssc.author), 1)

        self.assertEqual(ssc.author[0].given_name, "Matthias")
        self.assertEqual(ssc.author[0].family_name, "Probst")

        self.assertEqual(
            ssc.author[0].affiliation.name,
            "Karlsruhe Institute of Technology, Institute of Thermal Turbomachinery"
        )
