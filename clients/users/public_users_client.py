from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

from clients.authentification.authentification_client import AuthenticationClient
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    user: User

class CreateUserRequestDict(TypedDict):
    """
    Структура данных для запроса на создание пользователя:
        email: Электронная почта пользователя.
        password: Пароль пользователя.
        lastName: Фамилия пользователя.
        firstName: Имя пользователя.
        middleName: Отчество пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    API клиент для работы с публичными методами эндпоинта /api/v1/users.
    Предназначен для выполнения запросов, не требующих авторизации.
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания нового пользователя.

        Args:
            request (CreateRequestDict): Словарь с данными пользователя, содержащий
                поля email, password, lastName, firstName, middleName.

        Returns:
            Response: Объект ответа httpx.Response от сервера с результатами выполнения запроса.
        """
        return self.post(url="/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())
