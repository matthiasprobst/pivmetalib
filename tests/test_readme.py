import pathlib

import pivmetalib
import utils

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()


class TestReadme(utils.ClassTest):

    def test_code(self):
        from pivmetalib import pivmeta, prov

        software = pivmeta.PIVSoftware(
            author=prov.Organization(
                name='OpenPIV',
                url='https://github.com/OpenPIV/openpiv-python',
            ),
            description='OpenPIV is an open source Particle Image Velocimetry analysis software written in Python and Cython',
            softwareVersion="0.26.0a0",
            hasDocumentation='https://openpiv.readthedocs.io/en/latest/',
        )

        print(software.serialize("ttl"))
