from .. import sd, m4i
from ..model import namespaces, context


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@context(PIVSoftware='pivmeta:PIVSoftware')
class PIVSoftware(m4i.Tool, sd.Software):
    """Pydantic implementation of pivmeta:PIVSoftware

    PIVSoftware is a m4i:Tool. As m4i:Tool does not define properties,
    sd:Software is used as a dedicated Software description ontology
    """
