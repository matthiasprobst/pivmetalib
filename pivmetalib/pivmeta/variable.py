from datetime import datetime, date
from typing import Optional, Union, List

from ontolutils import namespaces, urirefs, Thing
from ontolutils.ex.m4i import TextVariable
from ontolutils.typing import ResourceType
from pydantic import Field, NonNegativeInt
from ssnolib.m4i import NumericalVariable


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(TemporalVariable='pivmeta:TemporalVariable',
         timeValue='pivmeta:timeValue')
class TemporalVariable(TextVariable):
    """A variable with a canonical time value (date or dateTimeStamp) given in piv:timeValue."""
    timeValue: Optional[Union[datetime, date, Union[List[date]], List[datetime]]] = Field(
        default=None,
        description="The canonical time value associated with this temporal variable.",
        alias="time_value"
    )


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Flag='pivmeta:Flag',
         mask='pivmeta:mask',
         meaning='pivmeta:meaning',
         )
class Flag(NumericalVariable):
    """flag atom"""
    mask: Optional[NonNegativeInt] = Field(
        default=None,
        description="Integer mask value representing the atomic flag."
    )
    meaning: Optional[str] = Field(
        default=None,
        description="Human-readable meaning of the atomic flag."
    )


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagValue='pivmeta:FlagValue',
    hasFlagValue='pivmeta:hasFlagValue',
)
class FlagValue(NumericalVariable):
    """Concrete stored value on data (bitmask or enumerated integer)."""
    hasFlagValue: Optional[NonNegativeInt] = Field(
        default=None,
        description="Concrete integer value stored with the data (bitwise OR of flag masks, or a single enumerated value).",
        alias="has flag value"
    )


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagMapping='pivmeta:FlagMapping',
    mapsToFlag='pivmeta:mapsToFlag',
    hasFlagValue='pivmeta:hasFlagValue',
)
class FlagMapping(Thing):
    """Associates a concrete integer value with a piv:Flag within a scheme."""
    mapsToFlag: Optional[Flag] = Field(
        default=None,
        description="Connects a piv:FlagMapping entry to the corresponding piv:Flag.",
        alias="maps_to_flag"
    )
    hasFlagValue: Optional[NonNegativeInt] = Field(
        default=None,
        description="Concrete integer value that maps to a specific atomic flag within the scheme.",
        alias="has_flag_value"
    )


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagSchemeType='pivmeta:FlagSchemeType',
)
class FlagSchemeType(Thing):
    """Superclass for scheme interpretation types (bitwise / enumerated)."""
    pass


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagScheme='pivmeta:FlagScheme',
    allowedFlag='pivmeta:allowedFlag',
    usesFlagSchemeType='pivmeta:usesFlagSchemeType',
    hasFlagMapping='pivmeta:hasFlagMapping',
)
class FlagScheme(Thing):
    """Declares the set of valid flags and how values are interpreted."""
    allowedFlag: Optional[List[Flag]] = Field(
        default=None,
        description="The atomic flags allowed in this scheme."
    )
    usesFlagSchemeType: Optional[Union[FlagSchemeType, ResourceType]] = Field(
        default=None,
        description="Scheme type: bitwise or enumerated."
    )
    hasFlagMapping: Optional[List[FlagMapping]] = Field(
        default=None,
        description="Explicit value-to-flag mappings (useful for enumerations and lookups)."
    )


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    BitwiseFlagScheme='pivmeta:BitwiseFlagScheme',
)
class BitwiseFlagScheme(FlagSchemeType):
    """Bitwise interpretation: flags combine via OR; recover with AND using each flag's mask."""
    pass


@namespaces(pivmeta="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    EnumeratedFlagScheme='pivmeta:EnumeratedFlagScheme',
)
class EnumeratedFlagScheme(FlagSchemeType):
    """Enumerated interpretation: values represent mutually exclusive states."""
    pass
