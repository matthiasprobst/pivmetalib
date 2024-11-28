import pathlib
import unittest

import pivmetalib
from pivmetalib.app.example_databases import PersonJSONLDFileDatabase, SQLDatabase
from pivmetalib.prov import Person

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestApp(unittest.TestCase):

    def test_jsonld_file_database(self):
        # running tests on the concrete implementations:
        db = PersonJSONLDFileDatabase(file_location=__this_dir__ / 'tmp/databases/person')
        self.assertEqual(db.name, 'person')
        db.reset()
        self.assertDictEqual({}, db.fetch_all())
        p1 = Person(orcidId='0000-0001-2345-6789', firstName='John', lastName='Doe')
        p2 = Person(orcidId='1234-0001-5555-6789', firstName='Jane', lastName='Williams')
        db.save(p1)
        self.assertEqual(1, len(db.fetch_all()))
        db.save(p2)
        self.assertEqual(2, len(db.fetch_all()))
        res = db.query(orcidId='0000-0001-2345-6789')
        self.assertEqual(res[0], p1)
        # shutil.rmtree(db.db_dir)

    def test_jsonld_sql_database(self):
        # running tests on the concrete implementations:
        db = SQLDatabase(Person)
        db.reset()
        self.assertEqual(f"{Person.__name__}.db", db.db_uri)
        self.assertDictEqual({}, db.fetch_all())
        p = Person(orcidId='0000-0001-2345-6789', firstName='John', lastName='Doe')
        db.save(p)
        self.assertEqual(1, len(db.fetch_all()))
        self.assertEqual(db.fetch_all()[p.id], p)
        res = db.query(orcidId='0000-0001-2345-6789')
        self.assertEqual(res[0], p)
        db.delete(orcidId='0000-0001-2345-6789')
        res = db.query(orcidId='0000-0001-2345-6789')
        self.assertEqual(res, [])
