import pathlib
import rdflib
import time
from datetime import datetime

import ontolutils
import pivmetalib
import utils
from ontolutils.namespacelib import QUDT_UNIT, QUDT_KIND
from pivmetalib import pivmeta, m4i
from pivmetalib.ssno import StandardName

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


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
                                                             hasNumericalValue=4.2,
                                                             hasUnit=QUDT_UNIT.M_PER_SEC,
                                                             hasKindOfQuantity=QUDT_KIND.Velocity)
                                       )
        self.assertEqual(method3.hasParameter[0].hasNumericalValue, 4.2)
        self.assertEqual(method3.hasParameter[0].hasUnit, str(QUDT_UNIT.M_PER_SEC))
        self.assertEqual(method3.hasParameter[0].hasKindOfQuantity, str(QUDT_KIND.Velocity))

        method3.add_numerical_variable(dict(label='a float',
                                            hasNumericalValue=12.2,
                                            hasUnit=QUDT_UNIT.M_PER_SEC,
                                            hasKindOfQuantity=QUDT_KIND.Velocity))
        self.assertEqual(method3.hasParameter[1].hasNumericalValue, 12.2)

        method3.add_numerical_variable(m4i.NumericalVariable(label='another float',
                                                             hasNumericalValue=-5.2,
                                                             hasUnit=QUDT_UNIT.M_PER_SEC,
                                                             hasKindOfQuantity=QUDT_KIND.Velocity))
        self.assertEqual(method3.hasParameter[2].hasNumericalValue, -5.2)

    def test_variable(self):
        var1 = m4i.NumericalVariable(label='Name of the variable',
                                     name='var1',
                                     # not part of ontology and defined in model. will not add a namespace
                                     hasNumericalValue=4.2)
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, m4i.NumericalVariable)
        self.assertEqual(var1.label, 'Name of the variable')
        self.assertEqual(var1.hasNumericalValue, 4.2)

        jsonld_string = var1.model_dump_jsonld()
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
        var1 = m4i.NumericalVariable(hasNumericalValue=4.2)
        method2 = m4i.Method(label='method2', hasParameter=var1)
        self.assertIsInstance(method2, ontolutils.Thing)
        self.assertIsInstance(method2, m4i.Method)
        self.assertEqual(method2.label, 'method2')
        self.assertEqual(method2.hasParameter, var1)

        jsonld_string = method2.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)
        print(jsonld_string)

    def test_method_n_parameters(self):
        # method with 2 parameters:
        var1 = m4i.NumericalVariable(hasNumericalValue=4.2)
        var2 = m4i.NumericalVariable(hasNumericalValue=5.2)
        method3 = m4i.Method(label='method3', hasParameter=[var1, var2])
        self.assertIsInstance(method3, ontolutils.Thing)
        self.assertIsInstance(method3, m4i.Method)
        self.assertEqual(method3.label, 'method3')
        self.assertIsInstance(method3.hasParameter, list)
        self.assertEqual(method3.hasParameter, [var1, var2])

        jsonld_string = method3.model_dump_jsonld(
            context={
                "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
            }
        )
        self.check_jsonld_string(jsonld_string)

    def test_parameter_with_standard_name(self):
        sn1 = StandardName(standard_name='x_velocity',
                           description='x component of velocity',
                           canonical_units='m s-1')
        sn2 = StandardName(standard_name='y_velocity',
                           description='y component of velocity',
                           canonical_units='m s-1')
        var1 = m4i.NumericalVariable(hasNumericalValue=4.2, hasStandardName=sn1)
        var2 = m4i.NumericalVariable(hasNumericalValue=5.2, hasStandardName=sn2)
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, m4i.NumericalVariable)
        self.assertIsInstance(var2, m4i.NumericalVariable)
        self.assertEqual(var1.hasNumericalValue, 4.2)

        self.assertEqual(var1.hasStandardName, sn1)
        self.assertNotEqual(var1.hasStandardName, sn2)

        sn1 = StandardName(standard_name='x_velocity',
                           description='x component of velocity',
                           canonical_units='m s-1')
        sn2 = StandardName(standard_name='y_velocity',
                           description='y component of velocity',
                           canonical_units='m s-1')
        var1 = pivmeta.NumericalVariable(hasNumericalValue=4.2, hasStandardName=sn1)
        var2 = pivmeta.NumericalVariable(hasNumericalValue=5.2, hasStandardName=sn2)
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, pivmeta.NumericalVariable)
        self.assertEqual(var1.hasNumericalValue, 4.2)

        var1.hasStandardName = sn1

        method = m4i.Method(label='method1')
        method.hasParameter = [var1, var2]

        jsonld_string = method.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_ProcessingStep(self):
        ps1 = m4i.ProcessingStep(label='p1',
                                 startTime=datetime.now())
        time.sleep(1)
        ps2 = m4i.ProcessingStep(label='p2',
                                 startTime=datetime.now(),
                                 starts_with=ps1)

        self.assertTrue(ps2.startTime > ps1.startTime)
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
        self.assertEqual(ps3.partOf, ps2)

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
                                                          hasNumericalValue=4.2,
                                                          hasUnit=QUDT_UNIT.M_PER_SEC,
                                                          hasKindOfQuantity=QUDT_KIND.Velocity))
        self.assertEqual(tool.hasParameter[0].hasNumericalValue, 4.2)
        tool.add_numerical_variable(dict(label='a float',
                                         hasNumericalValue=12.2,
                                         hasUnit=QUDT_UNIT.M_PER_SEC,
                                         hasKindOfQuantity=QUDT_KIND.Velocity))
        self.assertEqual(tool.hasParameter[1].hasNumericalValue, 12.2)
