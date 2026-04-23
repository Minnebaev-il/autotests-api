from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    GetExercisesQuerySchema,
    CreateExercisesRequestSchema,
    GetExercisesResponseSchema,
    GetExerciseRequestSchema,
    GetExerciseResponseSchema,
    CreateExercisesResponseSchema,
    UpdateExercisesRequestSchema,
    UpdateExercisesResponseSchema
)
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """Клиент для работы с API заданий (exercises)."""

    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Выполняет HTTP-запрос для получения списка заданий по ID курса.
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос для получения информации об одном конкретном задании.
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExercisesRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на создание нового задания.
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> Response:
        """
        Выполняет HTTP-запрос на обновление данных существующего задания.
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True))

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Выполняет HTTP-запрос на удаление задания по его ID.
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        """
        Получает список заданий и возвращает результат в виде схемы.
        """
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, request: GetExerciseRequestSchema) -> GetExerciseResponseSchema:
        """
        Получает одно задание по ID и возвращает результат в виде схемы.
        """
        response = self.get_exercise_api(request.exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExercisesRequestSchema) -> CreateExercisesResponseSchema:
        """
        Создает новое задание и возвращает результат в виде схемы.
        """
        response = self.create_exercise_api(request)
        return CreateExercisesResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExercisesRequestSchema) -> UpdateExercisesResponseSchema:
        """
        Обновляет задание и возвращает результат в виде схемы.
        """
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExercisesResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Создает и настраивает клиент для работы с заданиями.
    """
    return ExercisesClient(client=get_private_http_client(user))