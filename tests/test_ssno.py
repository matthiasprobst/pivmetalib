import json
import pathlib
import yaml

import ontolutils
import pivmetalib
import utils
from ontolutils import QUDT_UNIT
from pivmetalib.qudt import parse_unit
from pivmetalib.ssno import StandardName, StandardNameTable

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()

snt_jsonld = """{
  "@context": {
    "owl": "http://www.w3.org/2002/07/owl#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "local": "http://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dct": "http://purl.org/dc/terms/",
    "prov": "http://www.w3.org/ns/prov#",
    "ssno": "https://matthiasprobst.github.io/ssno/"
  },
  "@type": "ssno:StandardNameTable",
  "dct:title": "OpenCeFaDB Fan Standard Name Table",
  "ssno:has_standard_names": [
    {
      "@type": "ssno:StandardName",
      "ssno:standard_name": "absolute_pressure",
      "dcterms:description": "Pressure is force per unit area. Absolute air pressure is pressure deviation to a total vacuum.",
      "canonical_units": "Pa",
      "@id": "local:39257b94-d31c-480e-a43c-8ae7f57fae6d"
    },
    {
      "@type": "ssno:StandardName",
      "ssno:standard_name": "ambient_static_pressure",
      "dcterms:description": "Static air pressure is the amount of pressure exerted by air that is not moving. Ambient static air pressure is the static air pressure of the surrounding air.",
      "canonical_units": "Pa",
      "@id": "local:0637ec26-310b-4b0a-bf4c-e51d4afccc7d"
    },
    {
      "@type": "ssno:StandardName",
      "ssno:standard_name": "ambient_temperature",
      "dcterms:description": "Air temperature is the bulk temperature of the air, not the surface (skin) temperature. Ambient air temperature is the temperature of the surrounding air.",
      "canonical_units": "K",
      "@id": "local:3286d041-a826-4776-9d25-065dae107b55"
    },
    {
      "@type": "ssno:StandardName",
      "ssno:standard_name": "auxiliary_fan_rotational_speed",
      "dcterms:description": "Number of revolutions of an auxiliary fan.",
      "canonical_units": "1/s",
      "@id": "local:2a521e9d-4481-4965-9b42-390db2da4c83"
    }
  ]
}"""


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

    def test_standard_name_table_from_jsonld(self):
        snt_jsonld_filename = pathlib.Path(__this_dir__, 'snt.json')
        with open(snt_jsonld_filename, 'w') as f:
            json.dump(json.loads(snt_jsonld), f)
        snt = StandardNameTable.parse(snt_jsonld_filename, fmt='jsonld')

        snt_jsonld_filename.unlink(missing_ok=True)
        self.assertEqual(snt.title, 'OpenCeFaDB Fan Standard Name Table')

    def test_standard_name_table_from_yaml(self):
        snt_yaml_data = {'name': 'SNT',
                         'standard_names': {'x_velocity': {'description': 'x component of velocity',
                                                           'canonical_unit': 'm s-1'},
                                            'y_velocity': {'description': 'y component of velocity',
                                                           'canonical_unit': 'm s-1'}}}
        with open('snt.yaml', 'w') as f:
            yaml.dump(snt_yaml_data, f)
        snt = StandardNameTable.parse('snt.yaml', fmt='yaml')
        self.assertEqual(snt.title, 'SNT')
        pathlib.Path('snt.yaml').unlink(missing_ok=True)

    def test_standard_name_table_from_xml(self):
        cf_contention = 'http://cfconventions.org/Data/cf-standard-names/current/src/cf-standard-name-table.xml'
        from pivmetalib.utils import download_file
        snt_xml_filename = download_file(cf_contention,
                                         dest_filename='snt.xml')
        snt_xml_filename = download_file(cf_contention,
                                         dest_filename='snt.xml',
                                         overwrite_existing=True)
        snt_xml_filename = download_file(cf_contention,
                                         dest_filename='snt.xml',
                                         overwrite_existing=False)
        snt_xml_filename.unlink(missing_ok=True)
        snt_xml_filename = download_file(cf_contention)
        print(snt_xml_filename)
        snt = StandardNameTable.parse(snt_xml_filename, fmt='xml')
        self.assertEqual(
            snt.contact['mbox'],
            'support@ceda.ac.uk')
        snt_xml_filename.unlink(missing_ok=True)
