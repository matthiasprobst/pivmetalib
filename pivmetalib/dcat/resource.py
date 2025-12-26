from typing import Union, Optional

from ontolutils import urirefs, namespaces
from ontolutils.ex.dcat import Resource as OntolutilsDcatResource
from ontolutils.typing import ResourceType
from pydantic import Field

from ..pivmeta import FlagScheme


@namespaces(
    piv="https://matthiasprobst.github.io/pivmeta#"
)
@urirefs(Resource='dcat:Resource',
         hasFlagScheme='piv:hasFlagScheme',
         )
class Resource(OntolutilsDcatResource):
    hasFlagScheme: Optional[Union[FlagScheme, ResourceType]] = Field(
        default=None,
        description="Flag scheme associated with this dataset",
        alias='has_flag_scheme'
    )
