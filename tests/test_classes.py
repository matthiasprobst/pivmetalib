import pathlib
import time
import unittest
from datetime import datetime

import rdflib

import ontolutils
import pivmetalib
from ontolutils import QUDT_UNIT
from ontolutils import urirefs, namespaces, Thing
from ontolutils.classes.decorator import URIRefManager
from pivmetalib import pivmeta, prov, m4i
from pivmetalib.m4i import NumericalVariable
from pivmetalib.qudt.unit import parse_unit
from pivmetalib.ssno import StandardName
from pivmetalib.ssno import StandardNameTable

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestPIVProcess(unittest.TestCase):

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
        with self.assertRaises(RuntimeError):
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

        @urirefs(Testclass2='https://www.example.com/Testclass2',
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
            author=prov.Organisation(
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

    def test_preprocessing_step(self):
        ps1 = m4i.ProcessingStep(label='p1', startTime=datetime.now())
        time.sleep(1)
        ps2 = m4i.ProcessingStep(label='p2', startTime=datetime.now())

        ps1.starts_with = ps2

        self.assertTrue(ps2.startTime > ps1.startTime)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, m4i.ProcessingStep)
        self.assertIsInstance(ps1.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps1.starts_with, m4i.ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = m4i.Tool(label='tool1')
        ps1.hasEmployedTool = tool
        print(ps1.model_dump_jsonld())

    def test_tool(self):
        tool = m4i.Tool(label='tool')
        tool.add_numerical_variable(
            NumericalVariable(
                label='myvar',
                hasNumericalValue=3.4,
                hasUnit='m/s',
                hasKindOfQuantity=QUDT_UNIT.M_PER_SEC
            )
        )
        self.assertIsInstance(tool.hasParameter[0], NumericalVariable)
        self.assertEqual(tool.hasParameter[0].label, 'myvar')
        self.assertEqual(tool.hasParameter[0].hasVariableDescription,
                         None)
        self.assertEqual(tool.hasParameter[0].hasNumericalValue,
                         3.4)
        # print(tool.model_dump_jsonld(context=CONTEXT))

    def test_piv_software(self):
        mycompany = pivmeta.PIVSoftware(
            author=prov.Organisation(
                name='My GmbH',
                mbox='info@mycompany.com',
                url='https://www.mycompany.com/'
            ),
        )
        self.assertEqual(mycompany.author.name, 'My GmbH')
        self.assertEqual(mycompany.author.mbox, 'info@mycompany.com')
        self.assertIsInstance(mycompany, ontolutils.Thing)
        self.assertIsInstance(mycompany, pivmeta.PIVSoftware)
        self.assertIsInstance(mycompany.author, ontolutils.Thing)
        self.assertIsInstance(mycompany.author, prov.Organisation)

        mycompany2 = pivmeta.PIVSoftware(
            author=[
                prov.Organisation(
                    name='My GmbH',
                    mbox='info@mycompany.com',
                    url='https://www.mycompany.com/'
                ),
                prov.Person(
                    firstName='John'
                )
            ],
        )
        self.assertIsInstance(mycompany2.author, list)
        self.assertIsInstance(mycompany2.author[0], ontolutils.Thing)
        self.assertIsInstance(mycompany2.author[0], prov.Organisation)
        self.assertEqual(mycompany2.author[0].name, 'My GmbH')
        self.assertEqual(mycompany2.author[0].mbox, 'info@mycompany.com')
        self.assertIsInstance(mycompany2.author[1], ontolutils.Thing)
        self.assertIsInstance(mycompany2.author[1], prov.Person)
        self.assertIsInstance(mycompany2, ontolutils.Thing)
        self.assertIsInstance(mycompany2, pivmeta.PIVSoftware)

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

    def test_PivDistribution(self):
        piv_dist = pivmeta.PivDistribution(label='piv_distribution',
                                           filenamePattern=r'img\d{4}_[a,b].tif')
        self.assertEqual(URIRefManager[pivmeta.PivDistribution]['filenamePattern'], 'pivmeta:filenamePattern')

        self.assertIsInstance(piv_dist, ontolutils.Thing)
        self.assertIsInstance(piv_dist, pivmeta.PivDistribution)
        self.assertEqual(piv_dist.label, 'piv_distribution')
        self.assertEqual(piv_dist.filenamePattern, r'img\d{4}_[a,b].tif')
        jsonld_string = piv_dist.model_dump_jsonld(
            context={
                "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
            }
        )
        found_dist = ontolutils.query(
            pivmeta.PivDistribution,
            data=jsonld_string,
            context={
                "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
            }
        )
        self.assertEqual(len(found_dist), 1)
        self.assertEqual(found_dist[0].label, 'piv_distribution')
        self.assertEqual(found_dist[0].filenamePattern, r'img\d{4}_[a,b].tif')


class TestSSNO(unittest.TestCase):

    def test_standard_name(self):
        sn = StandardName(standard_name='x_velocity',
                          description='x component of velocity',
                          unit=QUDT_UNIT.M_PER_SEC)  # 'm s-1'
        self.assertIsInstance(sn, ontolutils.Thing)
        self.assertIsInstance(sn, StandardName)
        self.assertEqual(sn.standard_name, 'x_velocity')
        self.assertEqual(sn.description, 'x component of velocity')
        self.assertEqual(sn.unit, str(parse_unit('m s-1')))

        sn = StandardName(standard_name='x_velocity',
                          description='x component of velocity',
                          unit='m s-1')
        self.assertEqual(sn.unit, str(parse_unit('m s-1')))

        with open('sn.jsonld', 'w') as f:
            f.write(sn.model_dump_jsonld())

        sn_loaded = ontolutils.query(StandardName, source='sn.jsonld')
        self.assertEqual(len(sn_loaded), 1)
        self.assertEqual(sn_loaded[0].standard_name, 'x_velocity')
        self.assertEqual(sn_loaded[0].description, 'x component of velocity')
        self.assertEqual(sn_loaded[0].unit, str(parse_unit('m s-1')))

        sn_loaded = StandardName.from_jsonld(data=sn.model_dump_jsonld())
        self.assertEqual(len(sn_loaded), 1)
        self.assertEqual(sn_loaded[0].standard_name, 'x_velocity')
        self.assertEqual(sn_loaded[0].description, 'x component of velocity')
        self.assertEqual(sn_loaded[0].unit, str(parse_unit('m s-1')))

        pathlib.Path('sn.jsonld').unlink(missing_ok=True)

    def test_standard_name_table(self):
        sn1 = StandardName(standard_name='x_velocity',
                           description='x component of velocity',
                           unit='m s-1')
        sn2 = StandardName(standard_name='y_velocity',
                           description='y component of velocity',
                           unit='m s-1')

        snt = StandardNameTable(has_standard_names=[sn1, sn2])
        with open('snt.json', 'w') as f:
            f.write(snt.model_dump_jsonld())

        snt_loaded = list(StandardNameTable.from_jsonld(data=snt.model_dump_jsonld(), limit=None))
        self.assertEqual(len(snt_loaded), 1)
        self.assertEqual(len(snt_loaded[0].has_standard_names), 2)
        self.assertEqual(snt_loaded[0].has_standard_names[0].standard_name, 'x_velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[0].description, 'x component of velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[0].unit, str(parse_unit('m s-1')))
        self.assertEqual(snt_loaded[0].has_standard_names[1].standard_name, 'y_velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[1].description, 'y component of velocity')
        self.assertEqual(snt_loaded[0].has_standard_names[1].unit, str(parse_unit('m s-1')))

        snt_loaded = StandardNameTable.from_jsonld(data=snt.model_dump_jsonld(), limit=1)
        self.assertEqual(len(snt_loaded.has_standard_names), 2)
        self.assertEqual(snt_loaded.has_standard_names[0].standard_name, 'x_velocity')
        self.assertEqual(snt_loaded.has_standard_names[0].description, 'x component of velocity')
        self.assertEqual(snt_loaded.has_standard_names[0].unit, str(parse_unit('m s-1')))
        self.assertEqual(snt_loaded.has_standard_names[1].standard_name, 'y_velocity')
        self.assertEqual(snt_loaded.has_standard_names[1].description, 'y component of velocity')
        self.assertEqual(snt_loaded.has_standard_names[1].unit, str(parse_unit('m s-1')))
        pathlib.Path('snt.json').unlink(missing_ok=True)
