from typing import List
from pydantic import BaseModel, Field, ConfigDict


from tools.faker import fake


class ExercisesSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesQuerySchema(BaseModel):
    """Параметры запроса для получения списка заданий."""
    model_config = ConfigDict(populate_by_name=True)

    courses_id: str = Field(alias="courseId")

class GetExerciseRequestSchema(BaseModel):
    """Параметры запроса для получения задания по exercise_id"""
    exercise_id: str

class GetExercisesResponseSchema(BaseModel):
    """Структура ответа при получении списка заданий."""
    exercises: List[ExercisesSchema]

class GetExerciseResponseSchema(BaseModel):
    """Структура ответа после успешного получения одного задания"""
    exercise: ExercisesSchema

class CreateExercisesRequestSchema(BaseModel):
    """Данные для создания нового задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int = Field(alias="minScore", default_factory=fake.min_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.sentence)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class CreateExercisesResponseSchema(BaseModel):
    """Структура ответа после успешного создания задания."""
    exercise: ExercisesSchema


class UpdateExercisesRequestSchema(BaseModel):
    """Данные для обновления существующего задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str | None = Field(default_factory=fake.sentence)
    max_score: int | None = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: int | None = Field(alias="minScore", default_factory=fake.max_score)
    order_index: int | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.sentence)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)

class UpdateExercisesResponseSchema(BaseModel):
    """Структура ответа после успешного обновления задания."""
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    courseId: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")