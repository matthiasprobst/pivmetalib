# OpenPIV integration and related projects

## Using pivmetalib with OpenPIV

[OpenPIV](https://github.com/OpenPIV/openpiv-python) evaluates PIV image pairs.
pivmetalib supplies Python models for describing recordings, equipment, software
and processing using the [PIVMeta vocabulary](https://matthiasprobst.github.io/pivmeta/).
Applications can serialize those descriptions as JSON-LD or RDF alongside their
numerical results. See the [OpenPIV metadata notebook](Describe_PIV_eval_with_openPIV.ipynb)
and [result-file notebook](Describe_PIV_Result_File.ipynb) for examples.

Metadata export can be an optional step after an OpenPIV evaluation. Keep the
existing numerical result file and associate a metadata document with it using
stable identifiers. Record the actual software version and processing settings,
source recordings, calibration, image-pair timing, coordinate conventions, units
and validation or replacement policy where applicable. Describing the software
alone does not capture a complete processing run or establish reproducibility.

Whether such export becomes a default in OpenPIV is an OpenPIV maintainer
decision. Installing pivmetalib does not enable an automatic OpenPIV export hook.
A proposed upstream integration should specify its supported OpenPIV versions,
metadata fields, output association and behavior when export fails, then validate
those choices against a small real processing example. See the original
[OpenPIV integration discussion](https://github.com/matthiasprobst/pivmetalib/issues/3).

## AeroX and common exchange formats

[AeroX](https://github.com/garyjpage/AeroX) defines a CSV-based exchange format
for aerodynamic data, with column descriptions, units and input/output roles,
and provides processing tools. PIVMeta defines a semantic vocabulary; pivmetalib
provides Python models for that vocabulary. These projects address related
parts of data exchange, but using them together needs an explicit mapping.

A useful first interoperability proposal would include:

1. A small AeroX PIV result file and a corresponding metadata document.
2. Mappings for quantities, units, coordinates and result identifiers, with a
   clear account of which information stays in each file.
3. Processing and measurement provenance, including timing and calibration.
4. Validation showing that the association preserves the intended meaning and
   identifying information that cannot be represented or recovered.

There is currently no AeroX adapter in pivmetalib. A common-format agreement or
consortium also needs agreement from the participating projects; this library
does not establish either. The
[related-project discussion](https://github.com/matthiasprobst/pivmetalib/issues/8)
records the suggestion. A concrete mapping proposal with an example dataset can
be developed as a separate issue without committing projects to a new standard.

[Back to the README](../README.md)
