import json
import requests
from requests import Response
import jsonschema
from project_selene.utils.requests_helper import load_schema


def test_single_user():
    """ Query the user and get code status 200 """
    url = 'https://reqres.in/api/users/2'
    schema = load_schema('get_single_user.json')

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)

