import json
import pathlib
import pydantic
import rdflib
import ssnolib
import time
import unittest
from datetime import datetime

import pivmetalib
from pivmetalib import pivmeta, prov, m4i, owl

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
        ps1 = m4i.ProcessingStep(name='p1', start_time=datetime.now())
        time.sleep(1)
        ps2 = m4i.ProcessingStep(name='p2', start_time=datetime.now())

        ps1.starts_with = ps2
        with self.assertRaises(TypeError):
            ps1.starts_with = 123
        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, owl.Thing)
        self.assertIsInstance(ps1, m4i.ProcessingStep)
        self.assertIsInstance(ps1.starts_with, owl.Thing)
        self.assertIsInstance(ps1.starts_with, m4i.ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_piv_software(self):
        mycompany = pivmeta.PIVSoftware(
            author=prov.Organization(
                name='My GmbH',
                mbox='info@mycompany.com',
                url='https://www.mycompany.com/'
            ),
        )
        self.assertEqual(mycompany.author.name, 'My GmbH')
        self.assertEqual(mycompany.author.mbox, 'info@mycompany.com')
        self.assertIsInstance(mycompany, owl.Thing)
        self.assertIsInstance(mycompany, pivmeta.PIVSoftware)
        self.assertIsInstance(mycompany.author, owl.Thing)
        self.assertIsInstance(mycompany.author, prov.Organization)

        mycompany2 = pivmeta.PIVSoftware(
            author=[
                prov.Organization(
                    name='My GmbH',
                    mbox='info@mycompany.com',
                    url='https://www.mycompany.com/'
                ),
                prov.Person(
                    first_name='John'
                )
            ],
        )
        self.assertIsInstance(mycompany2.author, list)
        self.assertIsInstance(mycompany2.author[0], owl.Thing)
        self.assertIsInstance(mycompany2.author[0], prov.Organization)
        self.assertEqual(mycompany2.author[0].name, 'My GmbH')
        self.assertEqual(mycompany2.author[0].mbox, 'info@mycompany.com')
        self.assertIsInstance(mycompany2.author[1], owl.Thing)
        self.assertIsInstance(mycompany2.author[1], prov.Person)
        self.assertIsInstance(mycompany2, owl.Thing)
        self.assertIsInstance(mycompany2, pivmeta.PIVSoftware)

    def test_variable(self):
        var1 = m4i.Variable(value=4.2)
        self.assertIsInstance(var1, owl.Thing)
        self.assertIsInstance(var1, m4i.Variable)
        self.assertEqual(var1.value, 4.2)

        jsonld_string = var1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    def test_method_no_parameters(self):
        # method without parameters:
        method1 = m4i.Method(name='method1')
        self.assertIsInstance(method1, owl.Thing)
        self.assertIsInstance(method1, m4i.Method)
        self.assertEqual(method1.name, 'method1')

        jsonld_string = method1.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_method_one_parameters(self):
        # method with 1 parameter:
        var1 = m4i.Variable(value=4.2)
        method2 = m4i.Method(name='method2', has_parameter=var1)
        self.assertIsInstance(method2, owl.Thing)
        self.assertIsInstance(method2, m4i.Method)
        self.assertEqual(method2.name, 'method2')
        self.assertEqual(method2.has_parameter, var1)

        jsonld_string = method2.dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    def test_method_n_parameters(self):
        # method with 2 parameters:
        var1 = m4i.Variable(value=4.2)
        var2 = m4i.Variable(value=5.2)
        method3 = m4i.Method(name='method3', has_parameter=[var1, var2])
        self.assertIsInstance(method3, owl.Thing)
        self.assertIsInstance(method3, m4i.Method)
        self.assertEqual(method3.name, 'method3')
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
        var1 = m4i.Variable(value=4.2, standard_name=sn1)
        var2 = m4i.Variable(value=5.2, standard_name=sn2)
        self.assertIsInstance(var1, owl.Thing)
        self.assertIsInstance(var1, m4i.Variable)
        self.assertIsInstance(var2, m4i.Variable)
        self.assertEqual(var1.value, 4.2)
        with self.assertRaises(AttributeError):
            self.assertEqual(var1.standard_name, sn1)

        sn1 = ssnolib.StandardName(standard_name='x_velocity',
                                   description='x component of velocity',
                                   canonical_units='m s-1')
        sn2 = ssnolib.StandardName(standard_name='y_velocity',
                                   description='y component of velocity',
                                   canonical_units='m s-1')
        var1 = pivmeta.Variable(value=4.2, standard_name=sn1)
        var2 = pivmeta.Variable(value=5.2, standard_name=sn2)
        self.assertIsInstance(var1, owl.Thing)
        self.assertIsInstance(var1, pivmeta.Variable)
        self.assertEqual(var1.value, 4.2)

        with self.assertRaises(pydantic.ValidationError):
            var1.standard_name = 123
        var1.standard_name = sn1

        method = m4i.Method(name='method1')
        method.has_parameter = [var1, var2]

        jsonld_string = method.dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        print(jsonld_string)
