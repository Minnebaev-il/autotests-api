from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict


class CreateRequestDict(TypedDict):
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

    def create_user_api(self, request: CreateRequestDict) -> Response:
        """
        Выполняет POST-запрос к эндпоинту /api/v1/users для создания нового пользователя.

        Args:
            request (CreateRequestDict): Словарь с данными пользователя, содержащий
                поля email, password, lastName, firstName, middleName.

        Returns:
            Response: Объект ответа httpx.Response от сервера с результатами выполнения запроса.
        """
        return self.post(url="/api/v1/users", json=request)