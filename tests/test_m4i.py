import json
import pathlib
import time
import warnings
from datetime import datetime

import ontolutils
import pydantic
import rdflib
import requests
from ontolutils.ex.m4i import Tool, Method, ProcessingStep, NumericalVariable
from ontolutils.namespacelib import QUDT_UNIT, QUDT_KIND
from ssnolib import StandardName

import pivmetalib
import utils

__this_dir__ = pathlib.Path(__file__).parent

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
        method1 = Method(label='method1')
        self.assertEqual(method1.label, 'method1')
        self.assertIsInstance(method1, ontolutils.Thing)
        self.assertIsInstance(method1, Method)

        method2 = Method(label='method2')
        self.assertEqual(method2.label, 'method2')
        self.assertIsInstance(method2, ontolutils.Thing)
        self.assertIsInstance(method2, Method)

        method3 = Method(label='method3')
        self.assertEqual(method3.label, 'method3')
        self.assertIsInstance(method3, ontolutils.Thing)
        self.assertIsInstance(method3, Method)

        method3.add_numerical_variable(NumericalVariable(label='a float',
                                                         hasNumericalValue=4.2,
                                                         unit=str(QUDT_UNIT.M_PER_SEC),
                                                         quantity_kind=str(QUDT_KIND.Velocity))
                                       )
        self.assertEqual(method3.parameter[0].hasNumericalValue, 4.2)
        self.assertEqual(method3.parameter[0].unit, str(QUDT_UNIT.M_PER_SEC))
        self.assertEqual(method3.parameter[0].quantity_kind, str(str(QUDT_KIND.Velocity)))

        method3.add_numerical_variable(dict(label='a float',
                                            hasNumericalValue=12.2,
                                            unit=str(QUDT_UNIT.M_PER_SEC),
                                            quantity_kind=str(QUDT_KIND.Velocity)))
        self.assertEqual(method3.parameter[1].hasNumericalValue, 12.2)

        method3.add_numerical_variable(NumericalVariable(label='another float',
                                                         hasNumericalValue=-5.2,
                                                         unit=str(QUDT_UNIT.M_PER_SEC),
                                                         quantity_kind=str(QUDT_KIND.Velocity)))
        self.assertEqual(method3.parameter[2].hasNumericalValue, -5.2)

    def test_variable(self):
        var1 = NumericalVariable(label='Name of the variable',
                                 hasNumericalValue=4.2)
        print(var1.model_validate(dict(label='Name of the variable',
                                       hasNumericalValue=4.2)))
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, NumericalVariable)
        self.assertEqual(var1.label, 'Name of the variable')
        print(var1.model_dump_jsonld())
        self.assertEqual(var1.hasNumericalValue, 4.2)

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
        method1 = Method(label='method1')
        self.assertIsInstance(method1, ontolutils.Thing)
        self.assertIsInstance(method1, Method)
        self.assertEqual(method1.label, 'method1')

        jsonld_string = method1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_method_one_parameters(self):
        # method with 1 parameter:
        var1 = NumericalVariable(hasNumericalValue=4.2)
        method2 = Method(label='method2', parameters=var1)
        self.assertIsInstance(method2, ontolutils.Thing)
        self.assertIsInstance(method2, Method)
        self.assertEqual(method2.label, 'method2')
        self.assertEqual(method2.parameters, var1)

        jsonld_string = method2.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    if connected:
        def test_method_n_parameters(self):
            # method with 2 parameters:
            var1 = NumericalVariable(hasNumericalValue=4.2)
            var2 = NumericalVariable(hasNumericalValue=5.2)
            method3 = Method(label='method3', parameter=[var1, var2])
            self.assertIsInstance(method3, ontolutils.Thing)
            self.assertIsInstance(method3, Method)
            self.assertEqual(method3.label, 'method3')
            self.assertIsInstance(method3.parameter, list)
            self.assertEqual(method3.parameter, [var1, var2])

            self.assertEqual(
                method3.namespaces,
                {'owl': 'http://www.w3.org/2002/07/owl#',
                 'rdfs': 'http://www.w3.org/2000/01/rdf-schema#',
                 'm4i': 'http://w3id.org/nfdi4ing/metadata4ing#',
                 'skos': 'http://www.w3.org/2004/02/skos/core#',
                 'dcterms': 'http://purl.org/dc/terms/',
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
                 'skos': 'http://www.w3.org/2004/02/skos/core#',
                 'dcterms': 'http://purl.org/dc/terms/',
                 'schema': 'https://schema.org/'}
            )

            self.check_jsonld_string(jsonld_string)
            self.assertTrue('@import' in json.loads(jsonld_string)['@context'])

        def test_parameter_with_standard_name(self):
            sn1 = StandardName(standard_name='x_velocity',
                               description='x component of velocity',
                               unit='m s-1')
            sn2 = StandardName(standard_name='y_velocity',
                               description='y component of velocity',
                               unit='m s-1')
            var1 = NumericalVariable(hasNumericalValue=4.2, standard_name=sn1)
            var2 = NumericalVariable(hasNumericalValue=5.2, standard_name=sn2)
            self.assertIsInstance(var1, ontolutils.Thing)
            self.assertIsInstance(var1, NumericalVariable)
            self.assertIsInstance(var2, NumericalVariable)
            self.assertEqual(var1.hasNumericalValue, 4.2)

            self.assertEqual(var1.standard_name, sn1)
            self.assertNotEqual(var1.standard_name, sn2)

            sn1 = StandardName(standard_name='x_velocity',
                               description='x component of velocity',
                               unit='m s-1')
            sn2 = StandardName(standard_name='y_velocity',
                               description='y component of velocity',
                               unit='m s-1')
            var1 = NumericalVariable(hasNumericalValue=4.2, standard_name=sn1)
            var2 = NumericalVariable(hasNumericalValue=5.2, standard_name=sn2)
            self.assertIsInstance(var1, ontolutils.Thing)
            self.assertIsInstance(var1, NumericalVariable)
            self.assertEqual(var1.hasNumericalValue, 4.2)

            var1.standard_name = sn1

            method = Method(label='method1')
            method.parameter = [var1, var2]

            jsonld_string = method.model_dump_jsonld()
            self.check_jsonld_string(jsonld_string)

        def test_parameter_with_standard_name2(self):
            var_sn = NumericalVariable(
                hasNumericalValue=32.3,
                hasStandardName=StandardName(standard_name='x_velocity',
                                             description='x component of velocity',
                                             unit='m s-1')
            )
            print(var_sn.hasStandardName)

    def test_ProcessingStep(self):
        ps1 = ProcessingStep(label='p1',
                             startTime=datetime.now())
        time.sleep(1)
        ps2 = ProcessingStep(label='p2',
                             startTime=datetime.now(),
                             starts_with=ps1)

        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, ProcessingStep)

        self.assertIsInstance(ps2.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps2.starts_with, ProcessingStep)
        self.assertEqual(ps2.starts_with, ps1)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = Tool(label='tool1')
        ps1.hasEmployedTool = tool

        ps3 = ProcessingStep(label='p3',
                             startTime=datetime.now(),
                             hasEmployedTool=tool,
                             partOf=ps2)
        self.assertEqual(ps3.hasEmployedTool, tool)
        self.assertEqual(ps3.part_of, ps2)

        ps4 = ProcessingStep(label='p4',
                             starts_with=ps3.model_dump(exclude_none=True),
                             ends_with=ps2.model_dump(exclude_none=True))
        self.assertEqual(ps4.starts_with, ps3)

        with self.assertRaises(TypeError):
            ProcessingStep(label='p5',
                           starts_with=2.4)

        with self.assertRaises(TypeError):
            ProcessingStep(label='p5',
                           ends_with=2.4)

        tool.add_numerical_variable(NumericalVariable(label='a float',
                                                      hasNumericalValue=4.2,
                                                      unit=QUDT_UNIT.M_PER_SEC,
                                                      quantity_kind=str(QUDT_KIND.Velocity)))
        self.assertEqual(tool.parameter[0].hasNumericalValue, 4.2)
        tool.add_numerical_variable(dict(label='a float',
                                         hasNumericalValue=12.2,
                                         unit=QUDT_UNIT.M_PER_SEC,
                                         quantity_kind=str(QUDT_KIND.Velocity)))
        self.assertEqual(tool.parameter[1].hasNumericalValue, 12.2)

        ps4 = ProcessingStep(label='p4', hasOutput="https://example.org/123")
        self.assertEqual(ps4.hasOutput, "https://example.org/123")

        with self.assertRaises(pydantic.ValidationError):
            ProcessingStep(label='p4', hasOutput="123")
