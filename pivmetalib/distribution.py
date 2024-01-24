from pydantic import HttpUrl

from .dcat import Distribution


class PivDistribution(Distribution):
    """Implementation of pivmeta:PivDistribution

    Describes PIV data (images or result data). See also subclasses PivImageDistribution and PivResultDistribution.
    """


class PivResultDistribution(Distribution):
    """Implementation of pivmeta:PivResultDistribution

    Describes PIV result data (e.g. csv or hdf files) which are experimental or synthetic data.
    """


def make_href(url, text=None):
    """Returns a HTML link to the given URL"""
    if text:
        return f'<a href="{url}">{text}</a>'
    return f'<a href="{url}">{url}</a>'


class PivImageDistribution(Distribution):
    """Implementation of pivmeta:PivImageDistribution

    Describes PIV images (e.g. tiff files) which are experimental or synthetic data.
    """
    piv_image_type: HttpUrl

    def _repr_html_(self):
        """Returns the HTML representation of the class"""
        if str(self.piv_image_type) == "https://matthiasprobst.github.io/pivmeta#ExperimentalImage":
            pit = make_href("https://matthiasprobst.github.io/pivmeta#ExperimentalImage", "experimental")
            return f"{self.__class__.__name__}('{pit}', {make_href(self.download_URL)})"
        elif str(self.piv_image_type) == "https://matthiasprobst.github.io/pivmeta#SyntheticImage":
            pit = make_href("https://matthiasprobst.github.io/pivmeta#SyntheticImage", "synthetic")
            return f"{self.__class__.__name__}('{pit}', {make_href(self.download_URL)})"
        return f"{self.__class__.__name__}({make_href(self.download_URL)})"
