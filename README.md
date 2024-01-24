# pivmetalib

![Tests](https://github.com/matthiasprobst/pivmetalib/actions/workflows/tests.yml/badge.svg)
![DOCS](https://codecov.io/gh/matthiasprobst/pivmetalib/branch/main/graph/badge.svg)
![pyvers](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue)

A Python library to work with the [pivmeta ontology](https://matthiasprobst.github.io/pivmeta/).

## Installation

Currently, the library is not available on PyPI. Thus, you can install it directly from GitHub:

```bash
pip install git+https://github.com/matthiasprobst/pivmetalib.git
```

## Documentation and Usage

This library mainly implements the ontology in form of `pydantic` model classes. The *pivmeta* ontology uses other
ontologies and builds on top of them. Thus, some central classes from ontologies like *schema.org*, *prov*, *dcat* and
*m4i* are implemented, too. Have a look at the class diagram below (it may not be complete yet but gives a first idea).

Practical examples on how to use the library can be found in docs-folder (
e.g. [Describe a PIV recording](docs/Describe_a_PIV_recording.ipynb)).

![Class diagram](docs/class_structure.png)

## Contribution

Contributions are welcome. Please open an issue or a pull request.


