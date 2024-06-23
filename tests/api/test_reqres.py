import json

import allure
import pytest
import requests
from allure_commons.types import AttachmentType
from requests import Response
import jsonschema
from project_selene.utils.requests_helper import load_schema


def regress_api_get(url, **kwargs):
    with allure.step("API Request"):
        result = requests.get(url='https://reqres.in'+url, **kwargs)
        allure.attach(
            body=json.dumps(result.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.TEXT,
            extension='txt'
        )
        return result


def test_single_user():
    """ Query the user and get code status 200 """
    url = '/api/users/2'
    schema = load_schema('get_single_user.json')

    result: Response = regress_api_get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_single_user_id(id_):
    """ Query the user and get user id """
    url = f'/api/users/{id_}'

    result: Response = regress_api_get(url)
    assert result.json()['data']['id'] == id_


def test_list_of_users_pagination():
    """ The endpoint returns correct data for the given page number """
    page = 2
    per_page = 6
    url = '/api/users'

    result: Response = regress_api_get(
        url=url,
        params={"page": page, "per_page": per_page},
        headers={"Content-Type": "multipart/form-data"},
        json={},
        cookies={}
    )

    assert result.json()['page'] == page
    assert result.json()['per_page'] == per_page
    assert len(result.json()['data']) == per_page
