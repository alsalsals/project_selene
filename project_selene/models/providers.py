from project_selene.models.users import User


class UserProvider:
    def get_users(self) -> list[User]:
        raise NotImplementedError


class CsvUserProvider(UserProvider):
    def get_users(self) -> list[User]:
        pass
