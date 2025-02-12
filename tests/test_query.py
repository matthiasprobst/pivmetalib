import pathlib
import warnings

import ontolutils
import requests
from ontolutils import set_logging_level
from ssnolib.pimsii import Variable

import pivmetalib
from pivmetalib import PIV
from pivmetalib import dcat  # .dcat import Dataset, Distribution
from pivmetalib import pivmeta
from pivmetalib import prov  # Person

set_logging_level('DEBUG')
__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()
try:
    requests.get('https://github.com/', timeout=5)
    connected = True
except (requests.ConnectionError,
        requests.Timeout) as e:
    connected = False
    warnings.warn('No internet connection', UserWarning)

from utils import ClassTest


class TestQuery(ClassTest):
    if connected:
        def test_query_piv_dataset(self):
            ds = ontolutils.query(dcat.Dataset, self.test_jsonld_filename, limit=1)
            self.assertEqual(str(ds.landing_page), 'https://www.pivchallenge.org/pub/index.html#a')
            self.assertEqual(ds.id, "https://www.pivchallenge.org/pub/index.html#a")
            self.assertEqual(ds.label, "Challenge1A")
            self.assertEqual(ds.description, "Strong vortex (provided by Kaehler) < real > [1280 x 1024]")
            self.assertEqual(ds.qualifiedAttribution.hadRole, "http://w3id.org/nfdi4ing/metadata4ing#ContactPerson")
            self.assertEqual(ds.qualifiedAttribution.agent.mbox, "christian.kaehler@dlr.de")
            print(ds)

        def test_query(self):
            ds = dcat.Dataset(
                title='piv-challenge-1-C',
                creator=prov.Person(lastName='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),
                modified="2000-10-28",
                landingPage="https://www.pivchallenge.org/pub/index.html#c",
                description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
                distribution=[
                    pivmeta.ImageVelocimetryDistribution(
                        title='raw piv image data',
                        downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                        mediaType='application/zip',
                        pivImageType=PIV.SyntheticImage,
                        numberOfRecords=1,  # It contains one double image
                        filenamePattern="^C\d{3}_\d.tif$",  # the regex for the filename
                        hasMetric=Variable(label="image_bit_depth", value=8),
                    ),
                    pivmeta.ImageVelocimetryDistribution(
                        title='mask data',
                        downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                        mediaType='application/zip',
                        filenamePattern="^Cmask_1.tif$",  # the regex for the filename
                        hasMetric=Variable(label="image_bit_depth", value=8),
                    ),
                    dcat.Distribution(
                        title='ReadMe file',
                        downloadURL='https://www.pivchallenge.org/pub/E/readmeE.txt'
                    ),
                ]
            )

            with open('piv_challenge.jsonld', 'w') as f:
                json_ld_str = ds.model_dump_jsonld(
                    context={
                        "@import": 'https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld'
                    }
                )
                f.write(
                    json_ld_str
                )

            dist = ontolutils.query(
                pivmeta.ImageVelocimetryDistribution,
                source='piv_challenge.jsonld',
            )
            self.assertEqual(len(dist), 2)
            titles = [d.title for d in dist]
            filename_patterns = [d.filename_pattern for d in dist]
            self.assertIn('raw piv image data', titles)
            self.assertIn('^C\d{3}_\d.tif$', filename_patterns)

    def test_query_dataset(self):
        ds = dcat.Dataset(
            title='piv-challenge-1-C',
            creator=prov.Person(lastName='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),  # or =creator from above
            modified="2000-10-28",
            landingPage="https://www.pivchallenge.org/pub/index.html#c",
            description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
            distribution=[
                pivmeta.ImageVelocimetryDistribution(
                    title='raw piv image data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    pivImageType=PIV.SyntheticImage,
                    numberOfRecords=1,  # It contains one double image
                    filenamePattern=r"^C\d{3}_\d.tif$",  # the regex for the filename
                    imageBitDepth=8
                ),
                pivmeta.ImageVelocimetryDistribution(
                    title='mask data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    filenamePattern="^Cmask_1.tif$",  # the regex for the filename
                ),
                dcat.Distribution(
                    title='ReadMe file',
                    downloadURL='https://www.pivchallenge.org/pub/E/readmeE.txt'
                ),
            ]
        )
        with open('piv_challenge.jsonld', 'w') as f:
            json_ld_str = ds.model_dump_jsonld()
            f.write(
                json_ld_str
            )
        dss = ontolutils.query(dcat.Dataset, source='piv_challenge.jsonld')
        ds = dss[0]
