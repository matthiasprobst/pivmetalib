import json
import pathlib
import pydantic
import rdflib
import ssnolib
import time
import unittest
from datetime import datetime

import pivmetalib

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestPIVProcess(unittest.TestCase):

    def check_jsonld_string(self, jsonld_string):
        g = rdflib.Graph()
        g.parse(data=json.loads(jsonld_string), format='json-ld')
        self.assertTrue(len(g) > 0)
        for s, p, o in g:
            self.assertIsInstance(p, rdflib.URIRef)

    def test_preprocessing_step(self):
        ps1 = pivmetalib.ProcessingStep(label='p1', start_time=datetime.now())
        time.sleep(1)
        ps2 = pivmetalib.ProcessingStep(label='p2', start_time=datetime.now())

        ps1.starts_with = ps2
        with self.assertRaises(TypeError):
            ps1.starts_with = 123
        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, pivmetalib.Thing)
        self.assertIsInstance(ps1, pivmetalib.ProcessingStep)
        self.assertIsInstance(ps1.starts_with, pivmetalib.Thing)
        self.assertIsInstance(ps1.starts_with, pivmetalib.ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_variable(self):
        var1 = pivmetalib.Variable(value=4.2)
        self.assertIsInstance(var1, pivmetalib.Thing)
        self.assertIsInstance(var1, pivmetalib.Variable)
        self.assertEqual(var1.value, 4.2)

        jsonld_string = var1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    def test_method_no_parameters(self):
        # method without parameters:
        method1 = pivmetalib.Method(label='method1')
        self.assertIsInstance(method1, pivmetalib.Thing)
        self.assertIsInstance(method1, pivmetalib.Method)
        self.assertEqual(method1.label, 'method1')

        jsonld_string = method1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_method_one_parameters(self):
        # method with 1 parameter:
        var1 = pivmetalib.Variable(value=4.2)
        method2 = pivmetalib.Method(label='method2', has_parameter=var1)
        self.assertIsInstance(method2, pivmetalib.Thing)
        self.assertIsInstance(method2, pivmetalib.Method)
        self.assertEqual(method2.label, 'method2')
        self.assertEqual(method2.has_parameter, var1)

        jsonld_string = method2.dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    def test_method_n_parameters(self):
        # method with 2 parameters:
        var1 = pivmetalib.Variable(value=4.2)
        var2 = pivmetalib.Variable(value=5.2)
        method3 = pivmetalib.Method(label='method3', has_parameter=[var1, var2])
        self.assertIsInstance(method3, pivmetalib.Thing)
        self.assertIsInstance(method3, pivmetalib.Method)
        self.assertEqual(method3.label, 'method3')
        self.assertIsInstance(method3.has_parameter, list)
        self.assertEqual(method3.has_parameter, [var1, var2])

        jsonld_string = method3.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        jsonld_dict = json.loads(jsonld_string)
        self.assertEqual(len(jsonld_dict['@graph'][0]['has_parameter']), 2)

    def test_parameter_with_standard_name(self):
        sn1 = ssnolib.StandardName(standard_name='x_velocity',
                                   description='x component of velocity',
                                   canonical_units='m s-1')
        sn2 = ssnolib.StandardName(standard_name='y_velocity',
                                   description='y component of velocity',
                                   canonical_units='m s-1')
        var1 = pivmetalib.Variable(value=4.2, standard_name=sn1)
        var2 = pivmetalib.Variable(value=5.2, standard_name=sn2)
        self.assertIsInstance(var1, pivmetalib.Thing)
        self.assertIsInstance(var1, pivmetalib.Variable)
        self.assertEqual(var1.value, 4.2)
        self.assertEqual(var1.standard_name, sn1)

        with self.assertRaises(pydantic.ValidationError):
            var1.standard_name = 123
        var1.standard_name = sn1

        method = pivmetalib.Method(label='method1')
        method.has_parameter = [var1, var2]

        jsonld_string = method.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        print(jsonld_string)
