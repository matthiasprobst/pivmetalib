import h5rdmtoolbox as h5tbx
import unittest
from h5rdmtoolbox import jsonld

from pivmetalib import dcat  # .dcat import Dataset, Distribution
from pivmetalib import pivmeta  # import PivImageDistribution
from pivmetalib import prov  # Person
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
        # pprint(piv_software.dump_jsonld())
        # pprint(piv_software.model_dump_namespaced())
        with h5tbx.File('piv_software.h5', 'w') as h5:
            piv_software.dump_hdf(h5.create_group('my_piv_software'))
            h5.dumps()

        with h5tbx.File('piv_software.h5', 'r') as h5:
            print(jsonld.dumpd(h5['my_piv_software']))

    def test_dump_hdf2(self):
        ds = dcat.Dataset(
            id="https://www.pivchallenge.org/pub/index.html#c",
            title='piv-challenge-1-C',
            creator=prov.Person(lastName='Okamoto', mbox="okamoto@tokai.t.u-tokyo.ac.jp"),
            modified="2000-10-28",
            landingPage="https://www.pivchallenge.org/pub/index.html#c",
            description="Different velocity gradients with spatially varying image quality (provided by Okamoto) < synthetic > [256 x 128]",
            distribution=[
                pivmeta.PivImageDistribution(
                    title='raw data',
                    downloadURL='https://www.pivchallenge.org/pub/C/C.zip',
                    mediaType='application/zip',
                    pivImageType=PIVMETA.SyntheticImage
                ),
                dcat.Distribution(
                    title='ReadMe file',
                    downloadURL='https://www.pivchallenge.org/pub/E/readmeE.txt'
                ),
            ]
        )
        with h5tbx.File('piv_software.h5', 'w') as h5:
            ds.dump_hdf(h5.create_group('my_piv_software'))
            h5.dumps()
        from h5rdmtoolbox import jsonld
        with h5tbx.File('piv_software.h5', 'r') as h5:
            print(jsonld.dumpd(h5['my_piv_software']))
