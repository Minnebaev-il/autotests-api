from pydantic import BaseModel, Field, ConfigDict, HttpUrl
from tools.faker import fake
import uuid


class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreateFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    model_config = ConfigDict(populate_by_name=True)

    filename: str = Field(default_factory=lambda: f"{fake.uuid4()}.png")
    directory: str = Field(default="tests")
    upload_file: str

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema