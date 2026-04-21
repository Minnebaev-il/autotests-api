from httpx import Response
from typing import TypedDict

from clients.api_client import APIClient
from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client
from clients.users.private_users_client import User


class GetExercisesQueryDict(TypedDict):
    """Параметры запроса для получения списка заданий."""
    coursesId: str

class GetExercisesResponseDict(TypedDict):
    """Структура ответа при получении списка заданий."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExerciseRequestDict(TypedDict):
    """Параметры запроса для получения задания по exercise_id"""
    exercise_id: str

class GetExerciseResponseDict(TypedDict):
    """Структура ответа после успешного получения задания по exercise_id"""
    exercises: list[Exercise]

class CreateExercisesRequestDict(TypedDict):
    """Данные для создания нового задания."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class CreateExercisesResponseDict(TypedDict):
    """Структура ответа после успешного создания задания."""
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class UpdateExercisesRequestDict(TypedDict):
    """Данные для обновления существующего задания."""
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExercisesResponseDict(TypedDict):
    """Структура ответа после успешного обновления задания."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class ExercisesClient(APIClient):
    """Клиент для работы с API заданий (exercises)."""

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Выполняет HTTP-запрос для получения списка заданий по ID курса.

        Этот метод является низкоуровневой оберткой над GET-запросом.
        Возвращает сырой объект ответа, который необходимо обработать отдельно.

        :param query: Словарь, содержащий параметры запроса (ID курса в ключе 'coursesId').
        :return: Объект ответа сервера (httpx.Response).
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос для получения информации об одном конкретном задании.

        Этот метод является низкоуровневой оберткой над GET-запросом.
        Возвращает сырой объект ответа, который необходимо обработать отдельно.

        :param exercise_id: Уникальный идентификатор задания.
        :return: Объект ответа сервера (httpx.Response).
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Выполняет HTTP-запрос на создание нового задания.

        Этот метод является низкоуровневой оберткой над POST-запросом.
        Возвращает сырой объект ответа, который необходимо обработать отдельно.

        :param request: Словарь с данными нового задания (заголовок, ID курса, баллы и т.д.).
        :return: Объект ответа сервера (httpx.Response).
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Выполняет HTTP-запрос на обновление данных существующего задания.

        Этот метод является низкоуровневой оберткой над PATCH-запросом.
        Возвращает сырой объект ответа, который необходимо обработать отдельно.

        :param exercise_id: Уникальный идентификатор задания для обновления.
        :param request: Словарь с новыми данными задания (поля, которые нужно изменить).
        :return: Объект ответа сервера (httpx.Response).
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление задания по его ID.

        Этот метод является низкоуровневой оберткой над DELETE-запросом.
        Возвращает сырой объект ответа, который необходимо обработать отдельно.

        :param exercise_id: Уникальный идентификатор задания для удаления.
        :return: Объект ответа сервера (httpx.Response).
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Получает список заданий и возвращает результат в виде словаря.

        Этот метод является оберткой над get_exercises_api, которая сразу
        преобразует ответ сервера в удобный словарь (dict).

        :param query: Словарь, содержащий параметры запроса (ID курса в ключе 'coursesId').
        :return: Словарь со списком заданий.
        """
        response = self.get_exercises_api(query) # Исправлено имя метода вызова (было get_exercise_api)
        return response.json()

    def get_exercise(self, request: GetExerciseRequestDict) -> GetExerciseResponseDict:
        """
        Получает одно задание по ID и возвращает результат в виде словаря.

        Этот метод является оберткой над get_exercise_api, которая сразу
        преобразует ответ сервера в удобный словарь (dict).

        :param request: Словарь, содержащий ID задания (ключ 'exercise_id').
        :return: Словарь с данными полученного задания.
        """
        response = self.get_exercise_api(request['exercise_id']) # Исправлено имя метода и аргумент (было get_exercis_api и request)
        return response.json()

    def create_exercises(self, request: CreateExercisesRequestDict) -> CreateExercisesResponseDict:
        """
        Создает новое задание и возвращает результат в виде словаря.

        Этот метод является оберткой над create_exercise_api, которая сразу
        преобразует ответ сервера в удобный словарь (dict).

        :param request: Словарь с данными нового задания.
        :return: Словарь с данными созданного задания.
        """
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestDict) -> UpdateExercisesResponseDict:
        """
        Обновляет задание и возвращает результат в виде словаря.

        Этот метод является оберткой над update_exercise_api, которая сразу
        преобразует ответ сервера в удобный словарь (dict).

        :param exercise_id: Уникальный идентификатор задания для обновления.
        :param request: Словарь с новыми данными задания.
        :return: Словарь с данными обновленного задания.
        """
        response = self.update_exercise_api(exercise_id, request)
        return response.json()


# Добавляем builder для ExercisesClient
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создает и настраивает клиент для работы с заданиями.

    Функция автоматически подставляет нужные заголовки авторизации
    для указанного пользователя.

    :param user: Словарь с данными аутентификации пользователя.
    :return: Готовый к работе экземпляр ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))