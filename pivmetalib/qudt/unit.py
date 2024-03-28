import rdflib

from ontolutils import QUDT_UNIT

qudt_lookup = {
    's': QUDT_UNIT.SEC,  # time
    'm': QUDT_UNIT.M,  # length
    # derived units
    # velocity
    'm/s': QUDT_UNIT.M_PER_SEC,
    'm s-1': QUDT_UNIT.M_PER_SEC,
    'm*s-1': QUDT_UNIT.M_PER_SEC,
    'm*s^-1': QUDT_UNIT.M_PER_SEC,
    'm*s**-1': QUDT_UNIT.M_PER_SEC,
    # acceleration
    'm/s2': QUDT_UNIT.M_PER_SEC2,
    'm/s^2': QUDT_UNIT.M_PER_SEC2,
    'm/s**2': QUDT_UNIT.M_PER_SEC2,
    'm s^-2': QUDT_UNIT.M_PER_SEC2,
    'm s**-2': QUDT_UNIT.M_PER_SEC2,
    # velocity squared
    'm2/s2': QUDT_UNIT.M2_PER_SEC2,
    'm2/s^2': QUDT_UNIT.M2_PER_SEC2,
    'm2/s**2': QUDT_UNIT.M2_PER_SEC2,
    'm2 s^-2': QUDT_UNIT.M2_PER_SEC2,
    'm2 s**-2': QUDT_UNIT.M2_PER_SEC2,
    'm**2/s**2': QUDT_UNIT.M2_PER_SEC2,
    'm**2/s^2': QUDT_UNIT.M2_PER_SEC2,
    # dynamic viscosity
    'Pa s': QUDT_UNIT.PA_SEC,
    'Pa*s': QUDT_UNIT.PA_SEC,
    # kinematic viscosity
    'm2/s': QUDT_UNIT.M2_PER_SEC,
    'm2 s-1': QUDT_UNIT.M2_PER_SEC,
    'm2*s-1': QUDT_UNIT.M2_PER_SEC,
    'm**2/s': QUDT_UNIT.M2_PER_SEC,
    'm**2 s-1': QUDT_UNIT.M2_PER_SEC,
    # area
    'm2': QUDT_UNIT.M2,
    'm^2': QUDT_UNIT.M2,
    'm**2': QUDT_UNIT.M2,
    'mm2': QUDT_UNIT.MilliM2,
    'mm^2': QUDT_UNIT.MilliM2,
    'mm**2': QUDT_UNIT.MilliM2,
    # volume
    'm3': QUDT_UNIT.M3,
    'm^3': QUDT_UNIT.M3,
    'm**3': QUDT_UNIT.M3,
    'mm3': QUDT_UNIT.MilliM3,
    'mm^3': QUDT_UNIT.MilliM3,
    'mm**3': QUDT_UNIT.MilliM3,
    # volume flow rate
    'm3/s': QUDT_UNIT.M3_PER_SEC,
    'm3 s-1': QUDT_UNIT.M3_PER_SEC,
    'm3*s-1': QUDT_UNIT.M3_PER_SEC,
    'm3*s^-1': QUDT_UNIT.M3_PER_SEC,
    'm3*s**-1': QUDT_UNIT.M3_PER_SEC,
    'm**3/s': QUDT_UNIT.M3_PER_SEC,
    'm**3 s-1': QUDT_UNIT.M3_PER_SEC,
    'm**3*s-1': QUDT_UNIT.M3_PER_SEC,
    # density
    'kg/m**3': QUDT_UNIT.KiloGM_PER_M3,
    'kg/m^3': QUDT_UNIT.KiloGM_PER_M3,
    'kg/m3': QUDT_UNIT.KiloGM_PER_M3,
    'kg m-3': QUDT_UNIT.KiloGM_PER_M3,
    'kg m^-3': QUDT_UNIT.KiloGM_PER_M3,
    'kg*m-3': QUDT_UNIT.KiloGM_PER_M3,
    'kg*m^-3': QUDT_UNIT.KiloGM_PER_M3,
    # per length
    '1/m': QUDT_UNIT.PER_M,
    'm-1': QUDT_UNIT.PER_M,
    'm^-1': QUDT_UNIT.PER_M,
    'm**-1': QUDT_UNIT.PER_M,
    # per length squared
    '1/m2': QUDT_UNIT.PER_M2,
    '1/m**2': QUDT_UNIT.PER_M2,
    '1/m^2': QUDT_UNIT.PER_M2,
    'm-2': QUDT_UNIT.PER_M2,
    'm^-2': QUDT_UNIT.PER_M2,
    'm**-2': QUDT_UNIT.PER_M2,
    # per length cubed
    '1/m3': QUDT_UNIT.PER_M3,
    '1/m**3': QUDT_UNIT.PER_M3,
    '1/m^3': QUDT_UNIT.PER_M3,
    'm-3': QUDT_UNIT.PER_M3,
    'm^-3': QUDT_UNIT.PER_M3,
    'm**-3': QUDT_UNIT.PER_M3,
    # per second
    '1/s': QUDT_UNIT.PER_SEC,
    '1 s-1': QUDT_UNIT.PER_SEC,
    '1*s-1': QUDT_UNIT.PER_SEC,
    '1*s^-1': QUDT_UNIT.PER_SEC,
    '1*s**-1': QUDT_UNIT.PER_SEC,
    's-1': QUDT_UNIT.PER_SEC,
    's^-1': QUDT_UNIT.PER_SEC,
    's**-1': QUDT_UNIT.PER_SEC,
    # per second squared
    '1/s**2': QUDT_UNIT.PER_SEC2,
    '1/s^2': QUDT_UNIT.PER_SEC2,
    's^-2': QUDT_UNIT.PER_SEC2,
    's-2': QUDT_UNIT.PER_SEC2,
    's**-2': QUDT_UNIT.PER_SEC2,
    # frequency
    'Hz': QUDT_UNIT.HZ,
    # energy
    'joule': QUDT_UNIT.J,
    'Joule': QUDT_UNIT.J,
    'J': QUDT_UNIT.J,
    # power
    'W': QUDT_UNIT.W,
    'watt': QUDT_UNIT.W,
    'Watt': QUDT_UNIT.W,
    # pressure
    'Pa': QUDT_UNIT.PA,
    'pascal': QUDT_UNIT.PA,
    'Pascal': QUDT_UNIT.PA,
    # mass
    'kg': QUDT_UNIT.KiloGM,
    'kilogram': QUDT_UNIT.KiloGM,
    'kilograms': QUDT_UNIT.KiloGM,
    'Kilogram': QUDT_UNIT.KiloGM,
    'Kilograms': QUDT_UNIT.KiloGM,
    # mass flow rate
    'kg/s': QUDT_UNIT.KiloGM_PER_SEC,
    'kg s-1': QUDT_UNIT.KiloGM_PER_SEC,
    'kg*s-1': QUDT_UNIT.KiloGM_PER_SEC,
    # temperature
    'K': QUDT_UNIT.K,
    'kelvin': QUDT_UNIT.K,
    'Kelvin': QUDT_UNIT.K,
    # torque
    'N m': QUDT_UNIT.N_M,
    'N*m': QUDT_UNIT.N_M,
    'rad': QUDT_UNIT.RAD,
    '': QUDT_UNIT.UNITLESS
}


def parse_unit(unit_str: str) -> rdflib.URIRef:
    """Return IRI for a unit str. E.g. 'm/s' returns QUDT_UNIT.M_PER_SEC"""
    return qudt_lookup[unit_str]
