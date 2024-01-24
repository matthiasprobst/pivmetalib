from pydantic import PositiveInt

from .. import m4i


class InterrogationMethod(m4i.Method):
    """Implementation of pivmeta:InterrogationMethod"""


class ImageManipulationMethod(m4i.Method):
    """Implementation of pivmeta:ImageManipulationMethod
    """


class ImageRotation(ImageManipulationMethod):
    """Implementation of pivmeta:ImageRotation
    """


class ImageFilter(ImageManipulationMethod):
    """Implementation of pivmeta:ImageRotation
    """


class MedianFilter(ImageFilter):
    """Implementation of pivmeta:MedianFilter
    """
    kernel_size: PositiveInt


class MinMaxFilter(ImageFilter):
    """Implementation of pivmeta:MedianFilter
    """
    minimum_pixel_count: PositiveInt
    maximum_pixel_count: PositiveInt
