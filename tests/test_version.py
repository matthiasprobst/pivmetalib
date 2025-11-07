import json
import pathlib
import unittest

import requests

import pivmetalib

__this_dir__ = pathlib.Path(__file__).parent


class TestVersion(unittest.TestCase):

    def setUp(self):
        self.this_version = 'x.x.x'
        setupcfg_filename = __this_dir__ / '../setup.cfg'
        with open(setupcfg_filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'version' in line:
                    self.this_version = line.split(' = ')[-1].strip()

    def test_version(self):
        this_version = 'x.x.x'
        setupcfg_filename = __this_dir__ / '../setup.cfg'
        with open(setupcfg_filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                if 'version' in line:
                    this_version = line.split(' = ')[-1].strip()
        self.assertEqual(pivmetalib.__version__, this_version)

    def test_codemeta(self):
        """checking if the version in codemeta.json is the same as the one of the toolbox"""

        with open(__this_dir__ / '../codemeta.json', 'r') as f:
            codemeta = json.loads(f.read())

        assert codemeta['version'] == pivmetalib.__version__

    def test_readme(self):
        """checking if the version in the README.md is the same as the one of the toolbox"""
        with open(__this_dir__ / '../README.md', 'r') as f:
            readme = f.read()

        pivmeta_version_splitted = self.this_version.split('.')
        pivmeta_version = '.'.join(pivmeta_version_splitted[:3])
        assert f"pivmeta-{pivmeta_version}-orange" in readme

    def test_ssno_url_exists(self):
        """checking if the ssno url exists"""
        _version = pivmetalib.__version__.split('.')
        _ssno_version = f'{_version[0]}.{_version[1]}.{_version[2]}'
        url = f'https://matthiasprobst.github.io/pivmeta/{_ssno_version}/'
        assert requests.get(url).status_code == 200
