# Contribution

This repository is happy to take contributions.

## Adding or extending models

The models are subclasses of `pydantic.BaseModel`. If you want to add a new model or extend an existing one, please
use *pythonic* syntax for the model fields, even if the URI (IRI) is not pythonic.

For example, the field `schema:versionNumber` of an imaginary model `MyModel` should be defined as `version_number`.
We can do this by adding an alias like so:

```python
from pydantic import Field
from ontolutils import Thing, namespaces, urirefs


@namespaces(ex='http://example.org/',
            schema='http://schema.org/')
@urirefs(MyModel='ex:MyModel',
         schema='versionNumber')
class MyModel(Thing):
    version_number: str = Field(alias='schema:versionNumber')

```

The following will work:

```python
test = MyModel(version_number='1.0')
test = MyModel(versionNumber='1.0')
```

The JSON-LD string will look exactly the same in both cases:

```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ex": "http://example.org/"
  },
  "@graph": [
    {
      "@id": "http://example.org/MyModel",
      "@type": "Thing",
      "schema:versionNumber": "1.0"
    }
  ]
}
```