import pathlib

import ontolutils
import pivmetalib
import utils
from ontolutils.ex.schema import SoftwareApplication, SoftwareSourceCode
from ontolutils.ex.schema.thing import Thing as SchemaThing

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestSchema(utils.ClassTest):

    def test_SchemaThing(self):
        thing1 = SchemaThing(label='thing1')
        self.assertEqual(thing1.label, 'thing1')
        self.assertIsInstance(thing1, ontolutils.Thing)

    def test_SoftwareApplication(self):
        sa = SoftwareApplication(label='software1',
                                 applicationCategory='Engineering')
        self.assertEqual(sa.label, 'software1')
        self.assertEqual(sa.application_category, 'Engineering')

        sa = SoftwareApplication(label='software1',
                                 applicationCategory='file://Engineering')
        self.assertEqual(sa.label, 'software1')
        self.assertEqual(sa.application_category, 'Engineering')

    def test_SoftwareSourceCode(self):
        ssc = SoftwareSourceCode(
            label='source1',
            codeRepository='git+https://https://github.com/matthiasprobst/pivmetalib',
            applicationCategory='file://Engineering')
        self.assertEqual(ssc.label, 'source1')
        self.assertEqual(ssc.code_repository, 'git+https://https://github.com/matthiasprobst/pivmetalib')
        self.assertEqual(ssc.application_category, 'Engineering')

        ssc = SoftwareSourceCode(
            label='source1',
            codeRepository='https://github.com/matthiasprobst/pivmetalib',
            applicationCategory='Engineering')
        self.assertEqual(ssc.label, 'source1')
        self.assertEqual(str(ssc.code_repository),
                         'https://github.com/matthiasprobst/pivmetalib')
        self.assertEqual(str(ssc.application_category), 'Engineering')
