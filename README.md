<div align="center">

# pivmetalib

[![Tests](https://github.com/matthiasprobst/pivmetalib/actions/workflows/tests.yml/badge.svg)](https://github.com/matthiasprobst/pivmetalib/actions/workflows/tests.yml)
[![Codecov](https://codecov.io/gh/matthiasprobst/pivmetalib/branch/main/graph/badge.svg)](https://codecov.io/gh/matthiasprobst/pivmetalib)
[![Python Versions](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue)](https://pypi.org/project/pivmetalib/)
[![PyPI Version](https://img.shields.io/badge/pivmeta-3.1.0-orange)](https://pypi.org/project/pivmetalib/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen)](docs/README.md)

A Python library and high-level interface to work with the [pivmeta ontology](https://matthiasprobst.github.io/pivmeta/).
It allows you to describe PIV recordings, software, hardware and other related entities in a state-of-the-art and
scientifically compliant way.


</div>

---

The library depends on [ontolutils](https://ontology-utils.readthedocs.io/en/latest/), which provides the 
object-oriented interface to the ontology and the JSON-LD serialization.

## 🚀 Quick Start

Install the package and create your first PIV metadata in minutes:

```bash
pip install pivmetalib
```

```python
from pivmetalib import pivmeta, prov

# Describe PIV software
software = pivmeta.PIVSoftware(
    author=prov.Organization(
        name='OpenPIV',
        url='https://github.com/OpenPIV/openpiv-python',
    ),
    description='OpenPIV is an open source Particle Image Velocimetry analysis software',
    softwareVersion="0.26.0a0",
    hasDocumentation='https://openpiv.readthedocs.io/en/latest/',
)

# Export to JSON-LD for FAIR data sharing
print(software.serialize("jsonld"))
```

---

## 📖 Table of Contents

- [What You Can Do with pivmetalib](#what-you-can-do-with-pivmetalib)
- [Installation](#installation)
- [User Guide](#user-guide)
- [Key Features](#key-features)
- [Examples](#examples)

---

## What You Can Do with pivmetalib

### For **Researchers**

- **Document PIV Experiments**: Create comprehensive metadata for your recordings, setups, and processing steps
- **FAIR Data Compliance**: Export standardized metadata that makes your data findable, accessible, interoperable, and
  reusable
- **Reproducible Research**: Capture complete experimental configurations for scientific reproducibility
- **Data Processing Pipelines**: Document complex PIV processing workflows with provenance
- **Tool Interoperability**: Enable metadata exchange between different PIV tools
- **Long-term Preservation**: Store metadata in standards-compliant formats (JSON-LD, TTL)

## Installation

### Basic Installation

The package is available on PyPI and can be installed via pip:

```bash
pip install pivmetalib
```

### Development Installation

For development or to access additional dependencies:

```bash
# Install with test dependencies
pip install pivmetalib[test]

# Install with all optional dependencies
pip install pivmetalib[complete]

# Install from source for development
git clone https://github.com/matthiasprobst/pivmetalib.git
cd pivmetalib
pip install -e .[test]
```

### Verify Installation

```python
import pivmetalib
print(f"pivmetalib version: {pivmetalib.__version__}")
```

---

## User Guide

Choose your path based on your background and goals:

### **New to PIV Metadata?**

1. Start with [Getting Started Tutorial](docs/GettingStarted.ipynb) - Learn basic concepts
2. [Describe Your First Recording](docs/Describe_a_PIV_recording.ipynb) - Complete dataset workflow
3. [PIV Processing with OpenPIV](docs/Describe_PIV_eval_with_openPIV.ipynb) - Processing pipeline documentation
4. [Result File Documentation](docs/Describe_PIV_Result_File.ipynb) - Publishing your results

---

## Key Features

### **Comprehensive PIV Metadata**

- **Hardware Description**: Digital cameras, lasers, optical components, objectives
- **Software Documentation**: PIV analysis tools, processing parameters, version control
- **Experimental Setups**: Virtual and experimental configurations
- **Processing Pipelines**: Complete PIV analysis workflows with provenance

### **Data Quality Management**

- **Flag Schemes**: Flexible flag system for data quality indicators
- **Validation**: Built-in type checking and constraint validation
- **Standard Names**: Integration with PIV standard name tables for consistent terminology

### **Format Flexibility**

- **Multiple Exports**: JSON-LD, Turtle (TTL), XML serialization
- **Namespace Support**: Integration with schema.org, PROV, DCAT, M4I ontologies
- **Query Capabilities**: SPARQL queries and data retrieval from JSON-LD files

### **FAIR Compliance**

- **Findable**: Rich metadata with standardized identifiers
- **Accessible**: Multiple export formats for different tools
- **Interoperable**: Ontology-based approach for data exchange
- **Reusable**: Complete provenance and documentation

---

## Examples

### **Quick Examples**

**Describe PIV Software:**

```python
from pivmetalib import pivmeta, prov

software = pivmeta.PIVSoftware(
    author=prov.Organization(name='OpenPIV'),
    softwareVersion="0.26.0a0",
    description='Open source Particle Image Velocimetry analysis software'
)
```

**Export to Different Formats:**

```python
# JSON-LD
jsonld_data = software.serialize("jsonld")

# Turtle (TTL)  
ttl_data = software.serialize("ttl")

# XML
xml_data = software.serialize("xml")
```

**Query Existing Metadata:**

```python
from ontolutils import query
from pivmetalib.pivmeta import PIVSoftware

# Find all PIV software in a file
software_list = query(cls=PIVSoftware, source='metadata.jsonld')
```

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

---

## Acknowledgments

- Built on [ontolutils](https://ontology-utils.readthedocs.io/en/latest/) for ontology handling
- Integrates with [pivmeta ontology](https://matthiasprobst.github.io/pivmeta/) for PIV metadata standards
- Uses ontologies
  from [schema.org](https://schema.org/), [PROV](https://www.w3.org/TR/prov-o/), [DCAT](https://www.w3.org/TR/vocab-dcat/),
  and [M4I](http://w3id.org/nfdi4ing/metadata4ing)


