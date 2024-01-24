import abc

from .core import Thing


class ImageType(Thing, abc.ABC):
    """ImageType class. Should not be used, only individuals of it"""
