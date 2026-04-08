import json
import jsonschema
import pytest
import os

def test_schema_validity():
    assert os.path.exists('schema.json')
    with open('schema.json', 'r') as f:
        schema = json.load(f)
    jsonschema.Draft7Validator.check_schema(schema)

def test_metadata_json_files():
    json_files = ['datacite.json', 'dataset_description.json', 'codemeta.json', 'datapackage.json']
    for jf in json_files:
        assert os.path.exists(jf), f"{jf} missing"
        with open(jf, 'r') as f:
            json.load(f)
