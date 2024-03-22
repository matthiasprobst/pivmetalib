import json
import pathlib
import time
from datetime import datetime

import ontolutils
import pivmetalib
import utils
from ontolutils.classes.decorator import URIRefManager
from pivmetalib import pivmeta, prov, m4i
from pivmetalib.ssno import StandardName

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestPivmeta(utils.ClassTest):

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

    def test_ProcessingStep(self):
        st1 = datetime.now()
        ps1 = m4i.ProcessingStep(id='_:p1', label='p1', startTime=st1)
        time.sleep(1)
        st2 = datetime.now()
        ps2 = m4i.ProcessingStep(id='_:p2', label='p2', startTime=st2)

        ps1.starts_with = ps2

        self.assertTrue(ps2.startTime > ps1.startTime)
        self.assertIsInstance(ps1, ontolutils.Thing)
        self.assertIsInstance(ps1, m4i.ProcessingStep)
        self.assertIsInstance(ps1.starts_with, ontolutils.Thing)
        self.assertIsInstance(ps1.starts_with, m4i.ProcessingStep)
        self.assertEqual(ps1.starts_with, ps2)

        jsonld_string = ps1.model_dump_jsonld()
        self.check_jsonld_string(jsonld_string)

        tool = m4i.Tool(id='_:t1', label='tool1')
        ps1.hasEmployedTool = tool
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

    def test_PivPostProcessing(self):
        data_smoothing = m4i.Method(
            id='_:ms1',
            name='Low-pass filtering',
            description='applies a low-pass filtering on the data using a Gaussian weighted kernel of specified width to reduce spurious noise.',
            hasParameter=m4i.NumericalVariable(id="_:param1", label='kernel', hasNumericalValue=2.0)
        )
        post = pivmeta.PivPostProcessing(
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
            "@type": "pivmeta:PivProcessingStep",
            "rdfs:label": "Post processing",
            "m4i:realizesMethod": {
                "@type": "m4i:Method",
                "schema:description": "applies a low-pass filtering on the data using a Gaussian weighted kernel of specified width to reduce spurious noise.",
                "m4i:hasParameter": {
                    "@type": "m4i:NumericalVariable",
                    "rdfs:label": "kernel",
                    "m4i:hasNumericalValue": "2.0",
                    "@id": "_:param1"
                },
                "name": "Low-pass filtering",
                "@id": "_:ms1"
            },
            "@id": "_:pp1"
        },
            json.loads(post.model_dump_jsonld()))

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

    def test_make_href(self):
        from pivmetalib.pivmeta.distribution import make_href
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#PivImageDistribution', 'pivImageDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#PivImageDistribution">pivImageDistribution</a>'
        )
        self.assertEqual(
            make_href('https://matthiasprobst.github.io/pivmeta#PivImageDistribution'),
            '<a href="https://matthiasprobst.github.io/pivmeta#PivImageDistribution">'
            'https://matthiasprobst.github.io/pivmeta#PivImageDistribution</a>'
        )

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

    def test_PivImageDistribution(self):
        piv_img_dist = pivmeta.PivImageDistribution(
            label='piv_image_distribution',
            pivImageType=pivmeta.PivImageType.ExperimentalImage,
            imageBitDepth=8,
            numberOfRecords=100
        )
        self.assertFalse(piv_img_dist.is_synthetic())
        self.assertIsInstance(piv_img_dist, ontolutils.Thing)
        self.assertIsInstance(piv_img_dist, pivmeta.PivImageDistribution)
        self.assertEqual(piv_img_dist.label, 'piv_image_distribution')
        self.assertEqual(str(piv_img_dist.pivImageType),
                         str(pivmeta.PivImageType.ExperimentalImage.value))
        self.assertEqual(piv_img_dist.imageBitDepth, 8)
        self.assertEqual(piv_img_dist.numberOfRecords, 100)
        jsonld_string = piv_img_dist.model_dump_jsonld(
            context={
                "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
            }
        )
        found_dist = ontolutils.query(
            pivmeta.PivImageDistribution,
            data=jsonld_string,
            context={
                "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
            }
        )
        self.assertEqual(len(found_dist), 1)
        self.assertEqual(found_dist[0].label, 'piv_image_distribution')
        self.assertEqual(str(found_dist[0].pivImageType),
                         str(pivmeta.PivImageType.ExperimentalImage.value))
        self.assertEqual(found_dist[0].imageBitDepth, 8)
        self.assertEqual(found_dist[0].numberOfRecords, 100)

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

        min_cam = pivmeta.DigitalCamera.build_minimal(
            label='camera2',
            sensor_pixel_size=[1000, 400],
            focal_length_mm=50,
            fnumber=1.4,
            ccd_pixel_size_um=5.5,
        )
        self.assertIsInstance(min_cam, ontolutils.Thing)
        self.assertIsInstance(min_cam, pivmeta.DigitalCamera)
        self.assertEqual(min_cam.label, 'camera2')
        found_sensor_pixel_width = False
        found_sensor_pixel_height = False

        for param in min_cam.hasParameter:
            if param.label == 'sensor_pixel_width':
                found_sensor_pixel_width = True
                self.assertIsInstance(param, m4i.NumericalVariable)
                self.assertEqual(param.hasNumericalValue, 1000)
            if param.label == 'sensor_pixel_height':
                found_sensor_pixel_height = True
                self.assertIsInstance(param, m4i.NumericalVariable)
                self.assertEqual(param.hasNumericalValue, 400)
        self.assertEqual(min_cam.fnumber, '1.4')
        self.assertTrue(found_sensor_pixel_height)
        self.assertTrue(found_sensor_pixel_width)
