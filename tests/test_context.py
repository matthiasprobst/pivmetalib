import unittest

from pydantic import HttpUrl

from pivmetalib import CONTEXT


class TestContext(unittest.TestCase):

    def test_context_url(self):
        self.assertTrue(HttpUrl(CONTEXT))
