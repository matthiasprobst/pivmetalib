import json

import unittest

from pivmetalib import CONTEXT
from pivmetalib import m4i
import rdflib

class TestJSONLD(unittest.TestCase):

    def test_correct_namespaces(self):
        dyn_mean = m4i.Method(
            name='dynamic mean test',
            has_parameter=[
                m4i.NumericalVariable(
                    name='mean',
                    has_numerical_value=2.0
                ),
                m4i.NumericalVariable(
                    name='var',
                    has_numerical_value=1.0
                )
            ]
        )
        jsonld_dict = json.loads(dyn_mean.dump_jsonld(context=CONTEXT))
        method_name = jsonld_dict['@graph'][0]['name']

        g = rdflib.Graph()
        g.parse(data=jsonld_dict, format='json-ld')

        for t in g:
            print(t)

        query = (f"""SELECT ?id
        WHERE {{
            ?id rdf:type m4i:Method .
        }}""")
        query_result = g.query(query)

        self.assertEqual(len(query_result), 1)

        for r in query_result:
            print(r)

        query = (f"""SELECT ?id
        WHERE {{
            ?id rdf:type m4i:Method .
            ?id schema:name "{method_name}" .
        }}""")
        query_result = g.query(query)

        # self.assertEqual(len(query_result), 1)

        for r in query_result:
            print(r)
