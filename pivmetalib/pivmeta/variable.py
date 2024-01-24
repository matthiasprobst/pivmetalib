from pydantic import HttpUrl
from ssnolib import StandardName
from typing import Union

from .. import m4i


class Variable(m4i.Variable):
    """Pydantic Model for m4i:Variable

    .. note::

        More than the below parameters are possible but not explicitly defined here.


    Parameters
    ----------
    standard_name: Union[StandardName, HttpUrl]
        The standard name of the variable
    """
    standard_name: Union[StandardName, HttpUrl] = None
