from abc import ABC, abstractmethod


class MySQLDatabase:

    def get(self, id_:int) -> str:
        return f"Row found {id_}"


class UserServiceBad:

    def __init__(self):
        self.db = MySQLDatabase() # tight coupling

    def get_user(self, id_:int) -> str:
        return self.db.get(id_)


class UserRepository(ABC):

    @abstractmethod
    def get(self, id_:int) -> str:
        pass


class MySQLRepository(UserRepository):
    def get(self, id_:int) -> str:
        return f"MySQL| User found with {id_}"

class RedisRepository(UserRepository):
    def get(self, id_:int) -> str:
        return f"Redis| User found with {id_}"

class PostGresRepository(UserRepository):
    def get(self, id_:int) -> str:
        return f"PostGres| User found with {id_}"

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository # Dependency Injection

    def get_user(self, id_:int) ->str:
        return self.repository.get(id_)


mysql_repo = MySQLRepository()
redis_repo = RedisRepository()

service_1 = UserService(mysql_repo)
print(service_1.get_user(5))

service_2 = UserService(redis_repo)
print(service_2.get_user(5))