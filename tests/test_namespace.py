import pathlib
import unittest
from rdflib import URIRef

from pivmetalib.namespace import PIVMETA

__this_dir__ = pathlib.Path(__file__).parent


class TestNamespace(unittest.TestCase):

    def test_namespace(self):
        self.assertIsInstance(PIVMETA.has_standard_names, URIRef)
        self.assertEqual(PIVMETA.has_standard_names,
                         URIRef('https://matthiasprobst.github.io/pivmeta#has_standard_names'))
        self.assertEqual(PIVMETA.standard_name, URIRef('https://matthiasprobst.github.io/pivmeta#standard_name'))
