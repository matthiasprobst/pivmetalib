import ast
import importlib
import json
import pathlib
import sys
import time
import warnings
from datetime import datetime
from typing import Union, List

import ontolutils
import requests
import ssnolib
from ontolutils import get_urirefs
from ontolutils.classes.decorator import URIRefManager
from ontolutils.ex import prov
from ontolutils.ex.dcat import Dataset
from rdflib import DCAT
from ssnolib import StandardName
from ssnolib.pimsii import Variable

import pivmetalib
import utils
from pivmetalib import pivmeta
from ontolutils.ex.m4i import ProcessingStep, Tool, Method, NumericalVariable
from pivmetalib.namespace import PIV

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()

try:
    requests.get('https://github.com/', timeout=5)
    connected = True
except (requests.ConnectionError,
        requests.Timeout) as e:
    connected = False
    warnings.warn('No internet connection', UserWarning)


class TestPIVmeta(utils.ClassTest):

    def test_python_classes(self):
        namespace_names = [str(n).split('#', 1)[-1] for n in list(PIV.__dict__.values())]
        pivmeta_module_folder = __this_dir__ / "../pivmetalib/pivmeta"

        sys.path.insert(0, str(pivmeta_module_folder.resolve().parent))
        module = importlib.import_module("pivmeta")
        ignore = ["NdYAGLaser", ]
        for filename in pivmeta_module_folder.glob("*.py"):
            if filename.name != "__init__.py":
                with open(filename, "r", encoding="utf-8") as f:
                    node = ast.parse(f.read(), filename=filename)
                classes = [n.name for n in ast.walk(node) if isinstance(n, ast.ClassDef)]
                for cls_name in classes:
                    if cls_name not in ignore:
                        cls = getattr(module, cls_name)
                        for iri in get_urirefs(cls).values():
                            if "pivmeta:" in iri:
                                self.assertIn(iri.split(":", 1)[-1], namespace_names,
                                              f'missing class: {iri.split(":", 1)[-1]}')
                        self.assertTrue(cls_name in namespace_names, f"Class {cls_name} in {filename} not in namespace")

    def test_PIVSoftware(self):
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

        mycompany = pivmeta.PIVSoftware(
            author=prov.Organization(
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
        self.assertIsInstance(mycompany.author, prov.Organization)

        mycompany2 = pivmeta.PIVSoftware(
            author=[
                prov.Organization(
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
        self.assertIsInstance(mycompany2.author[0], prov.Organization)
        self.assertEqual(mycompany2.author[0].name, 'My GmbH')
        self.assertEqual(mycompany2.author[0].mbox, 'info@mycompany.com')
        self.assertIsInstance(mycompany2.author[1], ontolutils.Thing)
        self.assertIsInstance(mycompany2.author[1], prov.Person)
        self.assertIsInstance(mycompany2, ontolutils.Thing)
        self.assertIsInstance(mycompany2, pivmeta.PIVSoftware)

    def test_NumericalVariable(self):
        var = NumericalVariable(value=4.2)
        self.assertIsInstance(var, ontolutils.Thing)
        self.assertIsInstance(var, NumericalVariable)
        self.assertEqual(var.value, 4.2)

        jsonld_string = var.model_dump_jsonld()
        print(jsonld_string)
        self.check_jsonld_string(jsonld_string)

    def test_ProcessingStep(self):
        st1 = datetime.now()
        ps1 = ProcessingStep(id='_:p1', label='p1', startTime=st1)
        time.sleep(1)
        st2 = datetime.now()
        ps2 = ProcessingStep(id='_:p2', label='p2', startTime=st2)

        ps1.starts_with = ps2

        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, ProcessingStep)
        self.assertIsInstance(ps1.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps1.starts_with, ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = Tool(id='_:t1', label='tool1')
        ps1.hasEmployedTool = tool
        self.assertDictEqual({"@context": {
            "owl": "http://www.w3.org/2002/07/owl#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "m4i": "http://w3id.org/nfdi4ing/metadata4ing#",
            'pivmeta': 'https://matthiasprobst.github.io/pivmeta#',
            "schema": "https://schema.org/",
            'skos': 'http://www.w3.org/2004/02/skos/core#',
            'dcterms': 'http://purl.org/dc/terms/',
            "obo": "http://purl.obolibrary.org/obo/"
        },
            "@type": "m4i:ProcessingStep",
            "rdfs:label": "p1",
            "schema:startTime": {'@type': 'http://www.w3.org/2001/XMLSchema#dateTime',
                                 '@value': st1.isoformat()},
            "obo:RO_0002224": {
                "@type": "m4i:ProcessingStep",
                "rdfs:label": "p2",
                "schema:startTime": {'@type': 'http://www.w3.org/2001/XMLSchema#dateTime',
                                     '@value': st2.isoformat()},
                "@id": "_:p2"
            },
            "m4i:hasEmployedTool": {
                "@type": "m4i:Tool",
                "rdfs:label": "tool1",
                "@id": "_:t1"
            },
            "@id": "_:p1"
        },
            json.loads(ps1.model_dump_jsonld()))

        prov.Person(firstName='John',
                    lastName='Doe',
                    wasRoleIn=ps1)

    def test_PIVPostProcessing(self):
        data_smoothing = Method(
            id='_:ms1',
            name='Low-pass filtering',
            description='applies a low-pass filtering on the data using a Gaussian weighted kernel of specified width to reduce spurious noise.',
            parameter=NumericalVariable(id="_:param1", label='kernel', hasNumericalValue=2.0)
        )
        post = pivmeta.PIVPostProcessing(
            id='_:pp1',
            label='Post processing',
            realizesMethod=data_smoothing
        )
        self.assertDictEqual({
            "@context": {
                "owl": "http://www.w3.org/2002/07/owl#",
                "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
                "m4i": "http://w3id.org/nfdi4ing/metadata4ing#",
                "schema": "https://schema.org/",
                "obo": "http://purl.obolibrary.org/obo/",
                "pivmeta": "https://matthiasprobst.github.io/pivmeta#",
                "pims": "http://www.molmod.info/semantics/pims-ii.ttl#",
                'skos': 'http://www.w3.org/2004/02/skos/core#',
                'dcterms': 'http://purl.org/dc/terms/',
            },
            "@type": "pivmeta:PIVProcessingStep",
            "rdfs:label": "Post processing",
            "m4i:realizesMethod": {
                "@type": "m4i:Method",
                "schema:description": "applies a low-pass filtering on the data using a Gaussian weighted kernel of specified width to reduce spurious noise.",
                "m4i:hasParameter": {
                    "@type": "m4i:NumericalVariable",
                    "rdfs:label": "kernel",
                    "m4i:hasNumericalValue": 2.0,
                    "@id": "_:param1"
                },
                "name": "Low-pass filtering",
                "@id": "_:ms1"
            },
            "@id": "_:pp1"
        },
            json.loads(post.model_dump_jsonld()))

    def test_parameter_with_standard_name(self):
        sn1 = StandardName(standardName='x_velocity',
                           description='x component of velocity',
                           unit='m s-1')
        sn2 = StandardName(standardName='y_velocity',
                           description='y component of velocity',
                           unit='m s-1')
        var1 = NumericalVariable(value=4.2, standard_name=sn1)
        var2 = NumericalVariable(value=5.2, standard_name=sn2)
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, NumericalVariable)
        self.assertIsInstance(var2, NumericalVariable)
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

        method = Method(label='method1')
        method.parameter = [var1, var2]

        jsonld_string = method.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_make_href(self):
        from pivmetalib.pivmeta.distribution import make_href
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#ImageVelocimetryDistribution', 'pivImageDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#ImageVelocimetryDistribution">pivImageDistribution</a>'
        )
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#ImageVelocimetryDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#ImageVelocimetryDistribution">'
            'https://matthiasprobst.github.io/pivmeta#ImageVelocimetryDistribution</a>'
        )

    def test_virtual_setup(self):
        camera = pivmeta.VirtualCamera(
            label='virtual_camera',
            manufacturer=dict(name='Virtual Camera Manufacturer'),
            model='Virtual Camera Model',
            serialNumber='123456'
        )
        laser = pivmeta.VirtualLaser(label="virtual_laser")
        software = pivmeta.PIVSoftware(
            label='virtual_software',
        )
        setup = pivmeta.VirtualSetup(
            has_part=[camera, laser],
            usesSoftware=software
        )
        self.assertEqual(setup.has_part[0], camera)
        self.assertEqual(setup.has_part[1], laser)
        self.assertEqual(setup.usesSoftware, software)

        jsonld_string = setup.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_describe_piv_image(self):
        camera = pivmeta.VirtualCamera()
        laser = pivmeta.VirtualLaser()
        setup = pivmeta.Setup(
            has_part=[camera, laser]
        )
        img_dist = pivmeta.ImageVelocimetryDistribution(
            image_bit_depth=16
        )
        ds = pivmetalib.pivmeta.ImageVelocimetryDataset(
            label="My PIV Dataset",
            has_part=[setup],
            distribution=img_dist
        )
        print(ds.serialize(format="ttl"))

    if connected:
        def test_VelocimetryDistribution(self):
            piv_dist = pivmeta.ImageVelocimetryDistribution(label='piv_distribution',
                                                            hasPIVDataType=PIV.ExperimentalImage,
                                                            filenamePattern=r'img\d{4}_[a,b].tif')
            self.assertIsInstance(piv_dist.hasPIVDataType, str)
            self.assertEqual(URIRefManager[pivmeta.ImageVelocimetryDistribution]['filenamePattern'],
                             'pivmeta:filenamePattern')

            self.assertIsInstance(piv_dist, ontolutils.Thing)
            self.assertIsInstance(piv_dist, pivmeta.ImageVelocimetryDistribution)
            self.assertEqual(piv_dist.label, 'piv_distribution')
            self.assertEqual(piv_dist.filename_pattern, r'img\d{4}_[a,b].tif')
            jsonld_string = piv_dist.model_dump_jsonld(
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            found_dist = ontolutils.query(
                pivmeta.ImageVelocimetryDistribution,
                data=jsonld_string,
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            self.assertEqual(len(found_dist), 1)
            self.assertEqual(found_dist[0].label, 'piv_distribution')
            self.assertEqual(found_dist[0].filename_pattern, r'img\d{4}_[a,b].tif')

        def test_PIVImageDistribution_from_file(self):
            image_filename = __this_dir__ / 'testdata/piv_challenge.jsonld'
            assert image_filename.exists()
            image_dists = ontolutils.query(
                pivmeta.ImageVelocimetryDistribution,
                source=image_filename
            )
            self.assertIsInstance(image_dists[0], ontolutils.Thing)
            self.assertIsInstance(image_dists[0], pivmeta.ImageVelocimetryDistribution)
            has_correct_title = False
            for image_dist in image_dists:
                if image_dist.id == "http://example.org/d5b2d0c9-ba74-43eb-b68f-624e1183cb2d":
                    self.assertEqual(image_dist.title,
                                     "Raw PIV image data")
                    has_correct_title = True
            self.assertTrue(has_correct_title)

        def test_ImageVelocimetryDistribution(self):
            piv_img_dist = pivmeta.ImageVelocimetryDistribution(
                label='piv_image_distribution',
                hasPIVDataType=PIV.ExperimentalImage,
                hasMetric=Variable(label="image_bit_depth", value=8),
            )
            self.assertIsInstance(piv_img_dist, ontolutils.Thing)
            self.assertIsInstance(piv_img_dist, pivmeta.ImageVelocimetryDistribution)
            self.assertEqual(piv_img_dist.label, 'piv_image_distribution')
            self.assertEqual(str(piv_img_dist.hasPIVDataType),
                             str(PIV.ExperimentalImage))
            self.assertEqual(piv_img_dist.hasMetric.value, 8)
            jsonld_string = piv_img_dist.model_dump_jsonld(
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            found_dist = ontolutils.query(
                pivmeta.ImageVelocimetryDistribution,
                data=jsonld_string,
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            self.assertEqual(len(found_dist), 1)
            self.assertEqual(found_dist[0].label, 'piv_image_distribution')
            self.assertEqual(str(found_dist[0].hasPIVDataType),
                             str(PIV.ExperimentalImage))
            self.assertEqual(found_dist[0].hasMetric.value, '8')

    def test_Tool(self):
        tool = Tool(label='tool1')
        self.assertIsInstance(tool, ontolutils.Thing)
        self.assertIsInstance(tool, Tool)
        self.assertEqual(tool.label, 'tool1')

        jsonld_string = tool.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_DigitalCamera(self):
        camera = pivmeta.DigitalCamera(
            label='camera1',
            manufacturer=dict(name='Manufacturer1'),
            model='Model1',
            serialNumber='123456'
        )
        self.assertIsInstance(camera, ontolutils.Thing)
        self.assertIsInstance(camera, pivmeta.DigitalCamera)
        self.assertEqual(camera.label, 'camera1')

    def test_Setup(self):
        camera = pivmeta.DigitalCamera(
            label='camera1',
            manufacturer=dict(name='Manufacturer1'),
            model='Model1',
            serialNumber='123456'
        )
        laser = pivmeta.Laser(label="super duper laser")
        setup = pivmeta.Setup(
            has_part=[camera, laser]
        )
        self.assertEqual(setup.has_part[0], camera)
        self.assertEqual(setup.has_part[1], laser)

    def test_PIVCatalog(self):
        Catalog = ontolutils.build(
            namespace=DCAT._NS,
            namespace_prefix="dcat",
            class_name='Catalog',
            properties=[
                dict(name="dataset", property_type=Union[Dataset, List[Dataset]])
            ]
        )
        ds = Dataset(label='dataset1', distribution=[])

        piv_catalog = Catalog(dataset=ds)
        serialized = piv_catalog.serialize("ttl")
        expected_serialized = """@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

[] a dcat:Catalog ;
    dcat:dataset [ a dcat:Dataset ;
            rdfs:label "dataset1" ] .

"""
        self.assertEqual(serialized, expected_serialized)
