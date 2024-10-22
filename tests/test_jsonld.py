import json
import unittest
import warnings

import rdflib
import requests

from pivmetalib import CONTEXT
from pivmetalib import jsonld
from pivmetalib import m4i, prov


class TestJSONLD(unittest.TestCase):

    def setUp(self) -> None:
        self.maxDiff = None
        try:
            requests.get('https://github.com/', timeout=5)
            self.connected = True
        except (requests.ConnectionError,
                requests.Timeout) as e:
            self.connected = False
            warnings.warn('No internet connection', UserWarning)

    def test_merge(self):
        p1 = prov.Person(id='_:b1', firstName='John', lastName='Doe')
        p2 = prov.Person(id='_:b2', firstName='Jane', lastName='Doe')
        p12 = jsonld.merge([p1.model_dump_jsonld(), p2.model_dump_jsonld()])
        self.assertDictEqual({
            "@context": [
                {
                    "owl": "http://www.w3.org/2002/07/owl#",
                    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                    "m4i": 'http://w3id.org/nfdi4ing/metadata4ing#',
                    "schema": "https://schema.org/",
                    "prov": "http://www.w3.org/ns/prov#",
                    "foaf": "http://xmlns.com/foaf/0.1/"
                }
            ],
            "@graph": [
                {
                    "@type": "prov:Person",
                    "foaf:firstName": "John",
                    "foaf:lastName": "Doe",
                    "@id": "_:b1"
                },
                {
                    "@type": "prov:Person",
                    "foaf:firstName": "Jane",
                    "foaf:lastName": "Doe",
                    "@id": "_:b2"
                }
            ]
        },
            json.loads(p12))

    def test_correct_namespaces(self):
        dyn_mean = m4i.Method(
            name='dynamic mean test',
            parameter=[
                m4i.NumericalVariable(
                    name='mean',
                    value=2.0
                ),
                m4i.NumericalVariable(
                    name='var',
                    value=1.0
                )
            ]
        )
        if self.connected:
            jsonld_dict = json.loads(
                dyn_mean.model_dump_jsonld(
                    context={"@import": CONTEXT}
                )
            )

            g = rdflib.Graph()
            g.parse(
                data=jsonld_dict,
                format='json-ld')

            for t in g:
                print(t)

            query = (f"""SELECT ?id
            WHERE {{
                ?id rdf:type m4i:Method .
            }}""")
            query_result = g.query(query)

            self.assertEqual(len(query_result), 1)
