import pathlib
import unittest

import pivmetalib
from pivmetalib import PIVMETA  # the namespace module containing the URI addresses
from pivmetalib import dcat  # .dcat import Dataset, Distribution
from pivmetalib import pivmeta  # import PivImageDistribution
from pivmetalib import prov  # Person

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestQuery(unittest.TestCase):

    def test_query(self):
        ds = dcat.Dataset(
            title='piv-challenge-1-C',
            creator=prov.Person(lastName='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),
            modified="2000-10-28",
            landingPage="https://www.pivchallenge.org/pub/index.html#c",
            description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
            distribution=[
                pivmeta.PivImageDistribution(
                    title='raw piv image data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    pivImageType=PIVMETA.SyntheticImage,
                    numberOfRecords=1,  # It contains one double image
                    filenamePattern="^C\d{3}_\d.tif$",  # the regex for the filename
                    bit_depth=8
                ),
                pivmeta.PivMaskDistribution(
                    title='mask data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    filenamePattern="^Cmask_1.tif$",  # the regex for the filename
                    bit_depth=8
                ),
                dcat.Distribution(
                    title='ReadMe file',
                    downloadURL='https://www.pivchallenge.org/pub/E/readmeE.txt'
                ),
            ]
        )

        with open('piv_challenge.jsonld', 'w') as f:
            json_ld_str = ds.dump_jsonld()
            f.write(
                ds.dump_jsonld()
            )

        dist = pivmetalib.query(pivmeta.PivImageDistribution, source='piv_challenge.jsonld')
        self.assertEqual(len(dist), 1)
        self.assertEqual(dist[0].title, 'raw piv image data')
        self.assertEqual(dist[0].filenamePattern, '^C\d{3}_\d.tif$')

        pathlib.Path('piv_challenge.jsonld').unlink(missing_ok=True)

    def test_query_dataset(self):
        ds = dcat.Dataset(
            title='piv-challenge-1-C',
            creator=prov.Person(lastName='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),  # or =creator from above
            modified="2000-10-28",
            landingPage="https://www.pivchallenge.org/pub/index.html#c",
            description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
            distribution=[
                pivmeta.PivImageDistribution(
                    title='raw piv image data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    pivImageType=PIVMETA.SyntheticImage,
                    numberOfRecords=1,  # It contains one double image
                    filenamePattern=r"^C\d{3}_\d.tif$",  # the regex for the filename
                    imageBitDepth=8
                ),
                pivmeta.PivMaskDistribution(
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
            json_ld_str = ds.dump_jsonld()
            f.write(
                ds.dump_jsonld()
            )
        dss = pivmetalib.query(dcat.Dataset, source='piv_challenge.jsonld')
        ds = dss[0]
