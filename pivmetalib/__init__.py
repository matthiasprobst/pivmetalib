import requests
from typing import Dict

from ._version import __version__
from .owl import Thing
from .utils import get_cache_dir

CONTEXT = "https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld"
CACHE_DIR = get_cache_dir()


def get_context_json() -> Dict:
    """Get the pivmeta context file as a dictionary."""
    r = requests.get(CONTEXT)
    return r.json()


__all__ = ('__version__',
           'Thing',
           'CONTEXT',
           'CACHE_DIR',
           )
