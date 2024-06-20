import json

import requests
from requests import Response
import jsonschema


def test_single_user():
    """ Query the user and get code status 200 """
    url = 'https://reqres.in/api/users/2'
    result: Response = requests.get(url)

    with open('get_single_user.json') as file:
        schema = json.load(file)
        jsonschema.validate(result.json(), schema)

    assert result.status_code == 200

