import csv
import pytest

from project_selene.models.providers import UserProvider, CsvUserProvider
from project_selene.models.users import User, USER_ADULT_AGE, Status, Worker


@pytest.fixture
def user_provider() -> UserProvider:
    return CsvUserProvider()


@pytest.fixture
def read_users(user_provider) -> list[User]:
    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")

        return [User(name=user['name'],
                     age=int(user['age']),
                     status=Status.worker,
                     items=user['items'])
                for user in users]


@pytest.fixture
def get_workers(read_users) -> list[User]:
    workers = [Worker(name=user.name, age=user.age, items=user.items)
               for user in read_users if user.status == Status.worker]
    return workers


def test_workers_are_adults(get_workers):
    """
    Test all workers are adult
    """
    for worker in get_workers:
        assert worker.is_adult(), f"Worker {worker.name} is elder than {USER_ADULT_AGE}"
