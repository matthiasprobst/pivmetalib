from typing import TYPE_CHECKING
from typing import Union, Optional

from ontolutils import urirefs, namespaces
from ontolutils.ex.dcat import Dataset as OntolutilsDataset
from ontolutils.ex.dcat import Distribution as OntolutilsDistribution
from ontolutils.ex.dcat import Resource as OntolutilsDcatResource
from ontolutils.typing import ResourceType
from pydantic import Field

if TYPE_CHECKING:
    from ..pivmeta import FlagScheme


@namespaces(
    piv="https://matthiasprobst.github.io/pivmeta#"
)
@urirefs(Resource='dcat:Resource',
         hasFlagScheme='piv:hasFlagScheme',
         )
class Resource(OntolutilsDcatResource):
    hasFlagScheme: Optional[Union["FlagScheme", ResourceType]] = Field(
        default=None,
        description="Flag scheme associated with this dataset",
        alias='has_flag_scheme'
    )


@namespaces(
    piv="https://matthiasprobst.github.io/pivmeta#"
)
@urirefs(Distribution='dcat:Distribution',
         hasFlagScheme='piv:hasFlagScheme',
         )
class Distribution(OntolutilsDistribution):
    hasFlagScheme: Optional[Union["FlagScheme", ResourceType]] = Field(
        default=None,
        description="Flag scheme associated with this dataset",
        alias='has_flag_scheme'
    )


@namespaces(
    piv="https://matthiasprobst.github.io/pivmeta#"
)
@urirefs(Dataset='dcat:Dataset',
         hasFlagScheme='piv:hasFlagScheme',
         )
class Dataset(OntolutilsDataset):
    hasFlagScheme: Optional[Union["FlagScheme", ResourceType]] = Field(
        default=None,
        description="Flag scheme associated with this dataset",
        alias='has_flag_scheme'
    )
