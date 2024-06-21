import json
import jsonschema


def load_schema(filepath):
    with open(filepath) as file:
        schema = json.load(file)
        return schema


