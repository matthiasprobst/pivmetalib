from datetime import datetime, date
from typing import Optional, Union, List

from ontolutils import namespaces, urirefs, Thing
from ontolutils.ex.m4i import TextVariable
from pydantic import Field, NonNegativeInt
from ssnolib.m4i import NumericalVariable


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(TemporalVariable='piv:TemporalVariable',
         timeValue='piv:timeValue')
class TemporalVariable(TextVariable):
    """A variable with a canonical time value (date or dateTimeStamp) given in piv:timeValue."""
    timeValue: Optional[Union[datetime, date, Union[List[date]], List[datetime]]] = Field(
        default=None,
        description="The canonical time value associated with this temporal variable.",
        alias="time_value"
    )


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(Flag='piv:Flag',
         mask='piv:mask',
         meaning='piv:meaning',
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


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagMapping='piv:FlagMapping',
    mapsToFlag='piv:mapsToFlag',
    hasFlagValue='piv:hasFlagValue',
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


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagSchemeType='piv:FlagSchemeType',
)
class FlagSchemeType(Thing):
    """Describes how flag values are interpreted (bitwise vs enumerated)."""
    pass


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    FlagScheme='piv:FlagScheme',
    allowedFlag='piv:allowedFlag',
    usesFlagSchemeType='piv:usesFlagSchemeType',
    hasFlagMapping='piv:hasFlagMapping',
)
class FlagScheme(Thing):
    """Declares the set of valid flags and how values are interpreted."""
    allowedFlag: Optional[List[Flag]] = Field(
        default=None,
        alias="allowed_flag",
        description="The atomic flags allowed in this scheme."
    )
    usesFlagSchemeType: Optional[FlagSchemeType] = Field(
        default=None,
        alias="uses_flag_scheme_type",
        description="Scheme type: bitwise or enumerated."
    )
    hasFlagMapping: Optional[List[FlagMapping]] = Field(
        default=None,
        alias="has_flag_mapping",
        description="Explicit value-to-flag mappings (useful for enumerations and lookups)."
    )

    def get_flags(self, mask: int) -> List[Flag]:
        if self.usesFlagSchemeType is None:
            raise ValueError("Flag scheme type is not defined.")
        scheme_type = self.usesFlagSchemeType
        if isinstance(scheme_type, BitwiseFlagScheme):
            out = []
            for flag in self.allowedFlag or []:
                if flag.mask is not None and (flag.mask & mask) != 0:
                    out.append(flag)
            return out
        elif isinstance(scheme_type, EnumeratedFlagScheme):
            out = []
            for flag in self.allowedFlag or []:
                if flag.mask == mask:
                    out.append(flag)
            mapping = self.hasFlagMapping or []
            for map_entry in mapping:
                if map_entry.hasFlagValue == mask and map_entry.mapsToFlag is not None:
                    out.append(map_entry.mapsToFlag)
            return out
        else:
            raise ValueError("Unknown flag scheme type.")


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    BitwiseFlagScheme='piv:BitwiseFlagScheme',
)
class BitwiseFlagScheme(FlagSchemeType):
    """Bitwise interpretation: flags combine via OR; recover with AND using each flag's mask."""


@namespaces(piv="https://matthiasprobst.github.io/pivmeta#")
@urirefs(
    EnumeratedFlagScheme='piv:EnumeratedFlagScheme',
)
class EnumeratedFlagScheme(FlagSchemeType):
    """Enumerated interpretation: values represent mutually exclusive states."""
    pass
