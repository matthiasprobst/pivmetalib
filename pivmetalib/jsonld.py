import json
from typing import List


def merge(jsonld_strings: List[str]) -> str:
    """Merge multiple json-ld strings into one json-ld string.

    .. note::

        It is not checked if the @id's are unique!


    Parameters
    ----------
    jsonld_strings : List[str]
        List of json-ld strings to merge.

    Returns
    -------
    str
        Merged json-ld string.

    """
    jsonld_dicts = [json.loads(jldd) for jldd in jsonld_strings]

    contexts = []
    for jldd in jsonld_dicts:
        if jldd['@context'] not in contexts:
            contexts.append(jldd['@context'])

    out = {'@context': contexts,
           '@graph': []}

    for jldd in jsonld_dicts:
        if '@graph' in jldd:
            out['@graph'].append(jldd['@graph'])
        else:
            data = dict(jldd.items())
            data.pop('@context')
            out['@graph'].append(data)

    return json.dumps(out, indent=2)
