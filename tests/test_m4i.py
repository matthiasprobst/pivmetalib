import json
import pathlib
import time
import warnings
from datetime import datetime

import ontolutils
import pydantic
import rdflib
import requests
from ontolutils.namespacelib import QUDT_UNIT, QUDT_KIND
from ssnolib import StandardName
from ssnolib.m4i import NumericalVariable

import pivmetalib
import utils
from pivmetalib import m4i

__this_dir__ = pathlib.Path(__file__).parent

from pivmetalib.m4i import ProcessingStep

CACHE_DIR = pivmetalib.utils.get_cache_dir()

try:
    requests.get('https://github.com/', timeout=5)
    connected = True
except (requests.ConnectionError,
        requests.Timeout) as e:
    connected = False
    warnings.warn('No internet connection', UserWarning)


class TestM4i(utils.ClassTest):

    def test_Method(self):
        method1 = m4i.Method(label='method1')
        self.assertEqual(method1.label, 'method1')
        self.assertIsInstance(method1, ontolutils.Thing)
        self.assertIsInstance(method1, m4i.Method)

        method2 = m4i.Method(label='method2')
        self.assertEqual(method2.label, 'method2')
        self.assertIsInstance(method2, ontolutils.Thing)
        self.assertIsInstance(method2, m4i.Method)

        method3 = m4i.Method(label='method3')
        self.assertEqual(method3.label, 'method3')
        self.assertIsInstance(method3, ontolutils.Thing)
        self.assertIsInstance(method3, m4i.Method)

        method3.add_numerical_variable(m4i.NumericalVariable(label='a float',
                                                             value=4.2,
                                                             unit=QUDT_UNIT.M_PER_SEC,
                                                             quantity_kind=QUDT_KIND.Velocity)
                                       )
        self.assertEqual(method3.parameter[0].value, 4.2)
        self.assertEqual(method3.parameter[0].unit, str(QUDT_UNIT.M_PER_SEC))
        self.assertEqual(method3.parameter[0].quantity_kind, str(QUDT_KIND.Velocity))

        method3.add_numerical_variable(dict(label='a float',
                                            value=12.2,
                                            unit=QUDT_UNIT.M_PER_SEC,
                                            quantity_kind=QUDT_KIND.Velocity))
        self.assertEqual(method3.parameter[1].value, 12.2)

        method3.add_numerical_variable(m4i.NumericalVariable(label='another float',
                                                             value=-5.2,
                                                             unit=QUDT_UNIT.M_PER_SEC,
                                                             quantity_kind=QUDT_KIND.Velocity))
        self.assertEqual(method3.parameter[2].value, -5.2)

    def test_variable(self):
        var1 = m4i.NumericalVariable(label='Name of the variable',
                                     value=4.2)
        print(var1.model_validate(dict(label='Name of the variable',
                                       value=4.2)))
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, m4i.NumericalVariable)
        self.assertEqual(var1.label, 'Name of the variable')
        print(var1.model_dump_jsonld())
        self.assertEqual(var1.value, 4.2)

        jsonld_string = var1.model_dump_jsonld()
        print(jsonld_string)
        self.check_jsonld_string(jsonld_string)

        g = rdflib.Graph()
        g.parse(data=jsonld_string, format='json-ld',
                context={'m4i': 'http://w3id.org/nfdi4ing/metadata4ing#',
                         'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
                         'rdfs': 'http://www.w3.org/2000/01/rdf-schema#'})

    def test_method_no_parameters(self):
        # method without parameters:
        method1 = m4i.Method(label='method1')
        self.assertIsInstance(method1, ontolutils.Thing)
        self.assertIsInstance(method1, m4i.Method)
        self.assertEqual(method1.label, 'method1')

        jsonld_string = method1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_method_one_parameters(self):
        # method with 1 parameter:
        var1 = m4i.NumericalVariable(value=4.2)
        method2 = m4i.Method(label='method2', parameters=var1)
        self.assertIsInstance(method2, ontolutils.Thing)
        self.assertIsInstance(method2, m4i.Method)
        self.assertEqual(method2.label, 'method2')
        self.assertEqual(method2.parameters, var1)

        jsonld_string = method2.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    if connected:
        def test_method_n_parameters(self):
            # method with 2 parameters:
            var1 = m4i.NumericalVariable(value=4.2)
            var2 = m4i.NumericalVariable(value=5.2)
            method3 = m4i.Method(label='method3', parameter=[var1, var2])
            self.assertIsInstance(method3, ontolutils.Thing)
            self.assertIsInstance(method3, m4i.Method)
            self.assertEqual(method3.label, 'method3')
            self.assertIsInstance(method3.parameter, list)
            self.assertEqual(method3.parameter, [var1, var2])

            self.assertEqual(
                method3.namespaces,
                {'owl': 'http://www.w3.org/2002/07/owl#',
                 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                 'm4i': 'http://w3id.org/nfdi4ing/metadata4ing#',
                 'schema': 'https://schema.org/'}
            )
            jsonld_string = method3.model_dump_jsonld(
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            # the namespace must not be change for the same class after the above call
            self.assertEqual(
                method3.namespaces,
                {'owl': 'http://www.w3.org/2002/07/owl#',
                 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                 'm4i': 'http://w3id.org/nfdi4ing/metadata4ing#',
                 'schema': 'https://schema.org/'}
            )

            self.check_jsonld_string(jsonld_string)
            self.assertTrue('@import' in json.loads(jsonld_string)['@context'])

            print(method3.namespaces)
            print(method3.urirefs)

        def test_parameter_with_standard_name(self):
            sn1 = StandardName(standard_name='x_velocity',
                               description='x component of velocity',
                               unit='m s-1')
            sn2 = StandardName(standard_name='y_velocity',
                               description='y component of velocity',
                               unit='m s-1')
            var1 = m4i.NumericalVariable(value=4.2, standard_name=sn1)
            var2 = m4i.NumericalVariable(value=5.2, standard_name=sn2)
            self.assertIsInstance(var1, ontolutils.Thing)
            self.assertIsInstance(var1, m4i.NumericalVariable)
            self.assertIsInstance(var2, m4i.NumericalVariable)
            self.assertEqual(var1.value, 4.2)

            self.assertEqual(var1.standard_name, sn1)
            self.assertNotEqual(var1.standard_name, sn2)

            sn1 = StandardName(standard_name='x_velocity',
                               description='x component of velocity',
                               unit='m s-1')
            sn2 = StandardName(standard_name='y_velocity',
                               description='y component of velocity',
                               unit='m s-1')
            var1 = NumericalVariable(value=4.2, standard_name=sn1)
            var2 = NumericalVariable(value=5.2, standard_name=sn2)
            self.assertIsInstance(var1, ontolutils.Thing)
            self.assertIsInstance(var1, NumericalVariable)
            self.assertEqual(var1.value, 4.2)

            var1.standard_name = sn1

            method = m4i.Method(label='method1')
            method.parameter = [var1, var2]

            jsonld_string = method.model_dump_jsonld()
            self.check_jsonld_string(jsonld_string)

        def test_parameter_with_standard_name2(self):
            var_sn = NumericalVariable(
                value=32.3,
                hasStandardName=StandardName(standard_name='x_velocity',
                                             description='x component of velocity',
                                             unit='m s-1')
            )
            print(var_sn.hasStandardName)

    def test_ProcessingStep(self):
        ps1 = m4i.ProcessingStep(label='p1',
                                 startTime=datetime.now())
        time.sleep(1)
        ps2 = m4i.ProcessingStep(label='p2',
                                 startTime=datetime.now(),
                                 starts_with=ps1)

        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, m4i.ProcessingStep)

        self.assertIsInstance(ps2.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps2.starts_with, m4i.ProcessingStep)
        self.assertEqual(ps2.starts_with, ps1)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = m4i.Tool(label='tool1')
        ps1.hasEmployedTool = tool

        ps3 = m4i.ProcessingStep(label='p3',
                                 startTime=datetime.now(),
                                 hasEmployedTool=tool,
                                 partOf=ps2)
        self.assertEqual(ps3.hasEmployedTool, tool)
        self.assertEqual(ps3.part_of, ps2)

        ps4 = m4i.ProcessingStep(label='p4',
                                 starts_with=ps3.model_dump(exclude_none=True),
                                 ends_with=ps2.model_dump(exclude_none=True))
        self.assertEqual(ps4.starts_with, ps3)

        with self.assertRaises(TypeError):
            m4i.ProcessingStep(label='p5',
                               starts_with=2.4)

        with self.assertRaises(TypeError):
            m4i.ProcessingStep(label='p5',
                               ends_with=2.4)

        tool.add_numerical_variable(m4i.NumericalVariable(label='a float',
                                                          value=4.2,
                                                          unit=QUDT_UNIT.M_PER_SEC,
                                                          quantity_kind=QUDT_KIND.Velocity))
        self.assertEqual(tool.parameter[0].value, 4.2)
        tool.add_numerical_variable(dict(label='a float',
                                         value=12.2,
                                         unit=QUDT_UNIT.M_PER_SEC,
                                         quantity_kind=QUDT_KIND.Velocity))
        self.assertEqual(tool.parameter[1].value, 12.2)

        ps4 = ProcessingStep(label='p4', hasOutput="https://example.org/123")
        self.assertEqual(ps4.hasOutput, "https://example.org/123")

        with self.assertRaises(pydantic.ValidationError):
            ProcessingStep(label='p4', hasOutput="123")
