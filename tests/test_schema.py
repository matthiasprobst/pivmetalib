import pathlib

import ontolutils
import pivmetalib
import utils
from pivmetalib.schema import SoftwareApplication, SoftwareSourceCode
from pivmetalib.schema.thing import Thing as SchemaThing

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
        self.assertEqual(sa.applicationCategory, 'Engineering')

        sa = SoftwareApplication(label='software1',
                                 applicationCategory='file://Engineering')
        self.assertEqual(sa.label, 'software1')
        self.assertEqual(sa.applicationCategory, 'Engineering')

    def test_SoftwareSourceCode(self):
        ssc = SoftwareSourceCode(
            label='source1',
            codeRepository='git+https://https://github.com/matthiasprobst/pivmetalib',
            applicationCategory='file://Engineering')
        self.assertEqual(ssc.label, 'source1')
        self.assertEqual(ssc.codeRepository, 'git+https://https://github.com/matthiasprobst/pivmetalib')
        self.assertEqual(ssc.applicationCategory, 'Engineering')

        ssc = SoftwareSourceCode(
            label='source1',
            codeRepository='https://github.com/matthiasprobst/pivmetalib',
            applicationCategory='Engineering')
        self.assertEqual(ssc.label, 'source1')
        self.assertEqual(str(ssc.codeRepository),
                         'https://github.com/matthiasprobst/pivmetalib')
        self.assertEqual(str(ssc.applicationCategory), 'Engineering')
