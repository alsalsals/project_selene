import csv
import pytest


@pytest.fixture
def read_users():
    '''
    get all users from users.csv
    '''
    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")
        return users


@pytest.fixture
def get_workers(read_users):
    '''
    get workers from users.csv
    '''
    workers = [user for user in read_users if user['status'] == 'worker']
    return workers


def user_is_adult(worker):
    return int(worker['age']) >= 18


def test_workers_are_adults(get_workers):
    """
    Test all workers are adult
    """
    for worker in get_workers:
        assert user_is_adult, f"Worker {worker['name']} is elder than 18"





