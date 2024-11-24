import json
import pathlib
import time
from datetime import datetime

import ontolutils
from ontolutils.classes.decorator import URIRefManager

import pivmetalib
import utils
from pivmetalib import pivmeta, prov, m4i
from ssnolib import StandardName
import requests
import warnings
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
        var = m4i.NumericalVariable(value=4.2)
        self.assertIsInstance(var, ontolutils.Thing)
        self.assertIsInstance(var, m4i.NumericalVariable)
        self.assertEqual(var.value, 4.2)

        jsonld_string = var.model_dump_jsonld()
        print(jsonld_string)
        self.check_jsonld_string(jsonld_string)

    def test_ProcessingStep(self):
        st1 = datetime.now()
        ps1 = m4i.ProcessingStep(id='_:p1', label='p1', startTime=st1)
        time.sleep(1)
        st2 = datetime.now()
        ps2 = m4i.ProcessingStep(id='_:p2', label='p2', startTime=st2)

        ps1.starts_with = ps2

        self.assertTrue(ps2.start_time > ps1.start_time)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, m4i.ProcessingStep)
        self.assertIsInstance(ps1.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps1.starts_with, m4i.ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = m4i.Tool(id='_:t1', label='tool1')
        ps1.employed_tool = tool
        self.assertDictEqual({"@context": {
            "owl": "http://www.w3.org/2002/07/owl#",
            "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
            "m4i": "http://w3id.org/nfdi4ing/metadata4ing#",
            "schema": "https://schema.org/",
            "obo": "http://purl.obolibrary.org/obo/"
        },
            "@type": "m4i:ProcessingStep",
            "rdfs:label": "p1",
            "schema:startTime": st1.isoformat(),
            "obo:starts_with": {
                "@type": "m4i:ProcessingStep",
                "rdfs:label": "p2",
                "schema:startTime": st2.isoformat(),
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

        p = prov.Person(firstName='John',
                        lastName='Doe',
                        wasRoleIn=ps1)
        self.assertIsInstance(p.was_role_in, ontolutils.Thing)

    def test_PIVPostProcessing(self):
        data_smoothing = m4i.Method(
            id='_:ms1',
            name='Low-pass filtering',
            description='applies a low-pass filtering on the data using a Gaussian weighted kernel of specified width to reduce spurious noise.',
            parameter=m4i.NumericalVariable(id="_:param1", label='kernel', value=2.0)
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
        var1 = pivmeta.NumericalVariable(value=4.2, standard_name=sn1)
        var2 = pivmeta.NumericalVariable(value=5.2, standard_name=sn2)
        self.assertIsInstance(var1, ontolutils.Thing)
        self.assertIsInstance(var1, pivmeta.NumericalVariable)
        self.assertEqual(var1.value, 4.2)

        var1.standard_name = sn1

        method = m4i.Method(label='method1')
        method.parameter = [var1, var2]

        jsonld_string = method.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

    def test_make_href(self):
        from pivmetalib.pivmeta.distribution import make_href
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#PIVImageDistribution', 'pivImageDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#PIVImageDistribution">pivImageDistribution</a>'
        )
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#PIVImageDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#PIVImageDistribution">'
            'https://matthiasprobst.github.io/pivmeta#PIVImageDistribution</a>'
        )

    if connected:
        def test_PIVDistribution(self):
            piv_dist = pivmeta.PIVDistribution(label='piv_distribution',
                                               filenamePattern=r'img\d{4}_[a,b].tif')
            self.assertEqual(URIRefManager[pivmeta.PIVDistribution]['filenamePattern'], 'pivmeta:filenamePattern')

            self.assertIsInstance(piv_dist, ontolutils.Thing)
            self.assertIsInstance(piv_dist, pivmeta.PIVDistribution)
            self.assertEqual(piv_dist.label, 'piv_distribution')
            self.assertEqual(piv_dist.filename_pattern, r'img\d{4}_[a,b].tif')
            jsonld_string = piv_dist.model_dump_jsonld(
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            found_dist = ontolutils.query(
                pivmeta.PIVDistribution,
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
            image_dists = ontolutils.query(pivmeta.PIVImageDistribution, source=image_filename)
            self.assertIsInstance(image_dists[0], ontolutils.Thing)
            self.assertIsInstance(image_dists[0], pivmeta.PIVImageDistribution)
            has_correct_title = False
            for image_dist in image_dists:
                if image_dist.id == "http://example.org/d5b2d0c9-ba74-43eb-b68f-624e1183cb2d":
                    self.assertEqual(image_dist.title,
                                     "Raw PIV image data")
                    has_correct_title = True
            self.assertTrue(has_correct_title)

        def test_PIVImageDistribution(self):
            piv_img_dist = pivmeta.PIVImageDistribution(
                label='piv_image_distribution',
                pivImageType=pivmeta.PIVImageType.ExperimentalImage,
                imageBitDepth=8,
                numberOfRecords=100
            )
            self.assertFalse(piv_img_dist.is_synthetic())
            self.assertIsInstance(piv_img_dist, ontolutils.Thing)
            self.assertIsInstance(piv_img_dist, pivmeta.PIVImageDistribution)
            self.assertEqual(piv_img_dist.label, 'piv_image_distribution')
            self.assertEqual(str(piv_img_dist.piv_image_type),
                             str(pivmeta.PIVImageType.ExperimentalImage.value))
            self.assertEqual(piv_img_dist.image_bit_depth, 8)
            self.assertEqual(piv_img_dist.number_of_records, 100)
            jsonld_string = piv_img_dist.model_dump_jsonld(
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            found_dist = ontolutils.query(
                pivmeta.PIVImageDistribution,
                data=jsonld_string,
                context={
                    "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                }
            )
            self.assertEqual(len(found_dist), 1)
            self.assertEqual(found_dist[0].label, 'piv_image_distribution')
            self.assertEqual(str(found_dist[0].piv_image_type),
                             str(pivmeta.PIVImageType.ExperimentalImage.value))
            self.assertEqual(found_dist[0].image_bit_depth, 8)
            self.assertEqual(found_dist[0].number_of_records, 100)

    def test_Tool(self):
        tool = m4i.Tool(label='tool1')
        self.assertIsInstance(tool, ontolutils.Thing)
        self.assertIsInstance(tool, m4i.Tool)
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

    def test_PIVSetup(self):
        camera = pivmeta.DigitalCamera(
            label='camera1',
            manufacturer=dict(name='Manufacturer1'),
            model='Model1',
            serialNumber='123456'
        )
        laser = pivmeta.Laser(label="super duper laser")
        setup = pivmeta.PIVSetup(
            hasPart=[camera, laser]
        )
        self.assertEqual(setup.has_part[0], camera)
        self.assertEqual(setup.has_part[1], laser)