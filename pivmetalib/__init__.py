from ._version import __version__
from .owl import Thing
from .utils import get_cache_dir

CONTEXT = "https://raw.githubusercontent.com/matthiasprobst/pivmeta/main/pivmeta_context.jsonld"
CACHE_DIR = get_cache_dir()
__all__ = ('__version__',
           'Thing',
           'CONTEXT',
           'CACHE_DIR',
           )
