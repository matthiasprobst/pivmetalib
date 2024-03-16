import pathlib

import ontolutils
import pivmetalib
import utils
from ontolutils import QUDT_UNIT
from pivmetalib.qudt import parse_unit
from pivmetalib.ssno import StandardName, StandardNameTable

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestSSNO(utils.ClassTest):

    def test_standard_name(self):
        sn = StandardName(standard_name='x_velocity',
                          description='x component of velocity',
                          unit=QUDT_UNIT.M_PER_SEC)  # 'm s-1'
        self.assertIsInstance(sn, ontolutils.Thing)
        self.assertIsInstance(sn, StandardName)
        self.assertEqual(sn.standard_name, 'x_velocity')
        self.assertEqual(sn.description, 'x component of velocity')
        self.assertEqual(sn.unit, str(parse_unit('m s-1')))

        sn = StandardName(standard_name='x_velocity',
                          description='x component of velocity',
                          unit='m s-1')
        self.assertEqual(sn.unit, str(parse_unit('m s-1')))

        with open('sn.jsonld', 'w') as f:
            f.write(sn.model_dump_jsonld())

        sn_loaded = ontolutils.query(StandardName, source='sn.jsonld')
        self.assertEqual(len(sn_loaded), 1)
        self.assertEqual(sn_loaded[0].standard_name, 'x_velocity')
        self.assertEqual(sn_loaded[0].description, 'x component of velocity')
        self.assertEqual(sn_loaded[0].unit, str(parse_unit('m s-1')))

        sn_loaded = StandardName.from_jsonld(data=sn.model_dump_jsonld())
        self.assertEqual(len(sn_loaded), 1)
        self.assertEqual(sn_loaded[0].standard_name, 'x_velocity')
        self.assertEqual(sn_loaded[0].description, 'x component of velocity')
        self.assertEqual(sn_loaded[0].unit, str(parse_unit('m s-1')))

        pathlib.Path('sn.jsonld').unlink(missing_ok=True)

    def test_standard_name_table(self):
        sn1 = StandardName(standard_name='x_velocity',
                           description='x component of velocity',
                           unit='m s-1')
        sn2 = StandardName(standard_name='y_velocity',
                           description='y component of velocity',
                           unit='m s-1')

        snt = StandardNameTable(has_standard_names=[sn1, sn2])
        with open('snt.json', 'w') as f:
            f.write(snt.model_dump_jsonld())

        snt_loaded = list(StandardNameTable.from_jsonld(data=snt.model_dump_jsonld(), limit=None))
        self.assertEqual(len(snt_loaded), 1)
        self.assertEqual(len(snt_loaded[0].has_standard_names), 2)
        self.assertEqual(snt_loaded[0].has_standard_names[0].standard_name, 'x_velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[0].description, 'x component of velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[0].unit, str(parse_unit('m s-1')))
        self.assertEqual(snt_loaded[0].has_standard_names[1].standard_name, 'y_velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[1].description, 'y component of velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[1].unit, str(parse_unit('m s-1')))

        snt_loaded = StandardNameTable.from_jsonld(data=snt.model_dump_jsonld(), limit=1)
        self.assertEqual(len(snt_loaded.has_standard_names), 2)
        self.assertEqual(snt_loaded.has_standard_names[0].standard_name, 'x_velocity')
        self.assertEqual(snt_loaded.has_standard_names[0].description, 'x component of velocity')
        self.assertEqual(snt_loaded.has_standard_names[0].unit, str(parse_unit('m s-1')))
        self.assertEqual(snt_loaded.has_standard_names[1].standard_name, 'y_velocity')
        self.assertEqual(snt_loaded.has_standard_names[1].description, 'y component of velocity')
        self.assertEqual(snt_loaded.has_standard_names[1].unit, str(parse_unit('m s-1')))
        pathlib.Path('snt.json').unlink(missing_ok=True)
