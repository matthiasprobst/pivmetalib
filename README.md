# pivmetalib

![Tests](https://github.com/matthiasprobst/pivmetalib/actions/workflows/tests.yml/badge.svg)
![DOCS](https://codecov.io/gh/matthiasprobst/pivmetalib/branch/main/graph/badge.svg)
![pyvers](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)
![pivmeta](https://img.shields.io/badge/pivmeta-3.1.0-orange)

A Python library and high-level interface to work with the [pivmeta ontology](https://matthiasprobst.github.io/pivmeta/). 
It allows to describe PIV recordings, software, hardware and other related entities in a state-of-the-art and good
scientific practice compliant way.

The library depends on [ontolutils](https://ontology-utils.readthedocs.io/en/latest/), which provides the 
object-oriented interface to the ontology and the JSON-LD serialization.


## Usage

### Installation

The package is available on PyPI and can be installed via pip:
```bash
pip install pivmetalib
```

### Example of describing a PIV software:
It is very helpful to provide a description of the used PIV software together with the PIV recording. This can be done
using the `PIVSoftware` class from the `pivmeta` module. The following example shows how to describe the OpenPIV 
software. Put the resulting JSON-LD to your website, data repository or other places to make your data FAIR. 
Other users or software can then easily understand and use your data.

```python
from pivmetalib import pivmeta, prov

software = pivmeta.PIVSoftware(
    author=prov.Organization(
        name='OpenPIV',
        url='https://github.com/OpenPIV/openpiv-python',
    ),
    description='OpenPIV is an open source Particle Image Velocimetry analysis software written in Python and Cython',
    softwareVersion="0.26.0a0",
    hasDocumentation='https://openpiv.readthedocs.io/en/latest/',
)

print(software.serialize("ttl"))
```

This will result in the following TTL representation:

```turtle
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix pivmeta: <https://matthiasprobst.github.io/pivmeta#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema: <https://schema.org/> .
@prefix sd: <https://w3id.org/okn/o/sd#> .

[] a pivmeta:PIVSoftware ;
    schema:author [ a prov:Organization ;
            foaf:name "OpenPIV" ;
            schema:url <https://github.com/OpenPIV/openpiv-python> ] ;
    schema:description "OpenPIV is an open source Particle Image Velocimetry analysis software written in Python and Cython" ;
    schema:version "0.26.0a0" ;
    sd:hasDocumentation <https://openpiv.readthedocs.io/en/latest/> .
```


## Documentation and Usage

This library mainly implements the ontology in form of `pydantic` model classes. The *pivmeta* ontology uses other
ontologies and builds on top of them. Thus, some central classes from ontologies like *schema.org*, *prov*, *dcat* and
*m4i* are implemented, too.

Practical examples on how to use the library can be found in docs-folder (
e.g. [Describe a PIV recording](docs/Describe_a_PIV_recording.ipynb)).


## Contribution

Contributions are welcome. Please open an issue or a pull request.


