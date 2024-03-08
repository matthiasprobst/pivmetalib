import json
import unittest

import rdflib

from pivmetalib import CONTEXT
from pivmetalib import m4i


class TestJSONLD(unittest.TestCase):

    def test_correct_namespaces(self):
        dyn_mean = m4i.Method(
            name='dynamic mean test',
            hasParameter=[
                m4i.NumericalVariable(
                    name='mean',
                    hasNumericalValue=2.0
                ),
                m4i.NumericalVariable(
                    name='var',
                    hasNumericalValue=1.0
                )
            ]
        )
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
