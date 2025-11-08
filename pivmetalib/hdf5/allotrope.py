from typing import Optional, Union

from ontolutils import namespaces, urirefs
from ontolutils.ex.hdf5 import Dataset as BaseDataset
from ontolutils.typing import ResourceType
from pydantic import Field

from ..pivmeta import FlagScheme


@namespaces(
    pivmeta="https://matthiasprobst.github.io/pivmeta#",
    hdf5="http://purl.allotrope.org/ontologies/hdf5/1.8#",
)
@urirefs(
    Dataset='hdf5:Dataset',
    hasFlagScheme='pivmeta:hasFlagScheme',
)
class Dataset(BaseDataset):
    """Pydantic Model for Allotrope HDF5 Dataset"""
    hasFlagScheme: Optional[Union[FlagScheme, ResourceType]] = Field(
        default=None,
        description="Flag scheme associated with this dataset",
        alias='has_flag_scheme'
    )
