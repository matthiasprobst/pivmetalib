import pathlib
import unittest

import pydantic
import rdflib

import ontolutils
import pivmetalib
from ontolutils import urirefs, namespaces, Thing
from pivmetalib import pivmeta, prov

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestClasses(unittest.TestCase):

    def check_jsonld_string(self, jsonld_string):
        g = rdflib.Graph()
        g.parse(data=jsonld_string, format='json-ld',
                context={'m4i': 'http://w3id.org/nfdi4ing/metadata4ing#',
                         'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                         'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'})
        self.assertTrue(len(g) > 0)
        for s, p, o in g:
            self.assertIsInstance(p, rdflib.URIRef)

    def test_decorators(self):
        with self.assertRaises(pydantic.ValidationError):
            @namespaces(example='www.example.com/')
            @urirefs(Testclass='example:Testclass',
                     firstName='foaf:firstName')
            class Testclass(Thing):
                firstName: str

        @namespaces(example='https://www.example.com/')
        @urirefs(Testclass='example:Testclass',
                 firstName='foaf:firstName')
        class Testclass(Thing):
            firstName: str

        tc = Testclass(firstName='John')
        self.assertEqual(tc.firstName, 'John')
        self.assertDictEqual(
            pivmetalib.get_iri_fields(tc),
            {'Testclass': 'https://www.example.com/Testclass',
             'Thing': 'http://www.w3.org/2002/07/owl#Thing',
             'firstName': 'foaf:firstName',
             'label': 'http://www.w3.org/2000/01/rdf-schema#label'}
        )

        @namespaces(ex='https://www.example.com/')
        @urirefs(Testclass2='ex:Testclass2',
                 firstName='foaf:firstName')
        class Testclass2(Thing):
            firstName: str

        tc2 = Testclass2(firstName='John')
        self.assertEqual(tc2.firstName, 'John')
        self.assertDictEqual(
            pivmetalib.get_iri_fields(tc2),
            {'Testclass2': 'https://www.example.com/Testclass2',
             'Thing': 'http://www.w3.org/2002/07/owl#Thing',
             'firstName': 'foaf:firstName',
             'label': 'http://www.w3.org/2000/01/rdf-schema#label'}
        )

        @urirefs(name="http://example.com/name", age="http://example.com/age")
        class ExampleModel(Thing):
            name: str
            age: int

        em = ExampleModel(name="test", age=20)

        self.assertEqual(em.name, "test")
        self.assertEqual(em.age, 20)
        self.assertDictEqual(
            pivmetalib.get_iri_fields(em),
            {'Thing': 'http://www.w3.org/2002/07/owl#Thing',
             'label': 'http://www.w3.org/2000/01/rdf-schema#label',
             'name': 'http://example.com/name',
             'age': 'http://example.com/age'}
        )

    def test_serialization(self):
        pivtec = pivmeta.PIVSoftware(
            author=prov.Organization(
                name='PIVTEC GmbH',
                mbox='info@pivtec.com',
                url='https://www.pivtec.com/'
            ),
            has_documentation='https://www.pivtec.com/download/docs/PIVview_v36_Manual.pdf',
        )
        with open('software.jsonld', 'w') as f:
            f.write(pivtec.model_dump_jsonld())
        print(ontolutils.query(pivmeta.PIVSoftware, source='software.jsonld'))
        pathlib.Path('software.jsonld').unlink(missing_ok=True)
