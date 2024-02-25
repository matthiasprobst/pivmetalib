import h5rdmtoolbox as h5tbx
import unittest

from pivmetalib import pivmeta, prov
from pivmetalib import prov  # Person
from pivmetalib import dcat #.dcat import Dataset, Distribution
from pivmetalib import pivmeta # import PivImageDistribution
from pivmetalib.namespace import PIVMETA

class TestHDFDump(unittest.TestCase):

    def test_dump_hdf(self):
        piv_software = pivmeta.PIVSoftware(
            author=prov.Organisation(
                name='MyPIVSoftware GmbH',
                mbox='info@mypivsoftware.com',
                url='https://www.mypivsoftware.com/'
            ),
            has_documentation='https://www.mypivsoftware.com/download/docs/Manual.pdf',
        )
        from pprint import pprint
        # pprint(piv_software.dump_jsonld())
        # pprint(piv_software.model_dump_namespaced())
        with h5tbx.File('piv_software.h5', 'w') as h5:
            piv_software.dump_hdf(h5)
            h5.dumps()

    def test_dump_hdf2(self):
        ds = dcat.Dataset(
            title='piv-challenge-1-C',
            creator=prov.Person(last_name='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),
            modified="2000-10-28",
            landingPage="https://www.pivchallenge.org/pub/index.html#c",
            description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
            distribution=[
                pivmeta.PivImageDistribution(
                    title='raw data',
                    download_URL='https://www.pivchallenge.org/pub/C/C.zip',
                    media_type='application/zip',
                    piv_image_type=PIVMETA.SyntheticImage
                ),
                dcat.Distribution(
                    title='ReadMe file',
                    download_URL='https://www.pivchallenge.org/pub/E/readmeE.txt'
                ),
            ]
        )
        with h5tbx.File('piv_software.h5', 'w') as h5:
            ds.dump_hdf(h5)
            h5.dumps()
