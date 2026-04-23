from typing import List, Optional
from pydantic import BaseModel, Field, ConfigDict
import uuid


class ExercisesSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
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

    courses_id: str = Field(default_factory=lambda: str(uuid.uuid4()), alias="courseId")

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

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class CreateExercisesResponseSchema(BaseModel):
    """Структура ответа после успешного создания задания."""
    exercise: ExercisesSchema


class UpdateExercisesRequestSchema(BaseModel):
    """Данные для обновления существующего задания."""
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExercisesResponseSchema(BaseModel):
    """Структура ответа после успешного обновления задания."""
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    courseId: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")