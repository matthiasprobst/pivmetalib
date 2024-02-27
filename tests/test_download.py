import logging
import pathlib
import unittest

import pivmetalib
from pivmetalib.utils import download_file

__this_dir__ = pathlib.Path(__file__).parent
CACHE_DIR = pivmetalib.utils.get_cache_dir()

logger = logging.getLogger('pivmetalib')
logger.handlers[0].setLevel('DEBUG')


class TestDownload(unittest.TestCase):

    def test_download(self):
        ret = download_file('https://www.pivchallenge.org/pub/C/C.zip')
        self.assertTrue(ret.exists())
