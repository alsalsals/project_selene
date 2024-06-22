import pytest
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


@pytest.mark.parametrize('id_', [1, 2, 3])
def test_single_user_id(id_):
    """ Query the user and get user id """
    url = f'https://reqres.in/api/users/{id_}'

    result: Response = requests.get(url)

    # print(result.json()['data']['id'] == id_)
    assert result.json()['data']['id'] == id_


def test_list_of_users_pagination():
    """ The endpoint returns correct data for the given page number """
    page = 2
    per_page = 6
    url = f'https://reqres.in/api/users'
    token = "request.post(url, json={'user': 'Alex'}).json()[token]"

    result: Response = requests.get(
        url=url,
        params={"page": page, "per_page": per_page},
        headers={"Content-Type": "multipart/form-data", "Authorization": f"Bearer {token}"},
        json={},
        cookies={}
    )

    assert result.json()['page'] == page
    assert result.json()['per_page'] == per_page
    assert len(result.json()['data']) == per_page
