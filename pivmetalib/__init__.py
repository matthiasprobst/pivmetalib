import logging
import requests
from typing import Dict

from ._version import __version__
from .namespace import PIVMETA
from .owl import Thing
from .query_util import query
from .utils import get_cache_dir

DEFAULT_LOGGING_LEVEL = logging.WARNING
_formatter = logging.Formatter(
    '%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d_%H:%M:%S')

_stream_handler = logging.StreamHandler()
_stream_handler.setLevel(DEFAULT_LOGGING_LEVEL)
_stream_handler.setFormatter(_formatter)

logger = logging.getLogger(__package__)
logger.addHandler(_stream_handler)

CONTEXT = "https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld"
CACHE_DIR = get_cache_dir()


def get_context_json() -> Dict:
    """Get the pivmeta context file as a dictionary."""
    r = requests.get(CONTEXT)
    r.raise_for_status()
    return r.json()


__all__ = ('__version__',
           'Thing',
           'CONTEXT',
           'CACHE_DIR',
           'get_context_json',
           'PIVMETA'
           )
