import pathlib
import unittest
from rdflib import URIRef

from pivmetalib.namespace import PIVMETA, SSNO

__this_dir__ = pathlib.Path(__file__).parent


class TestNamespace(unittest.TestCase):

    def test_namespace(self):
        self.assertIsInstance(PIVMETA.has_standard_names, URIRef)
        self.assertEqual(PIVMETA.__dict__['has_standard_name'],
                         URIRef('https://matthiasprobst.github.io/pivmeta#hasStandardName'))
        with self.assertRaises(KeyError):
            self.assertEqual(PIVMETA.__dict__['standard_name'],
                             URIRef('https://matthiasprobst.github.io/pivmeta#standard_name'))
        self.assertEqual(SSNO.__dict__['standard_name'],
                         URIRef('https://matthiasprobst.github.io/ssno#standard_name'))
