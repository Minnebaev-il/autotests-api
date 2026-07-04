from pydantic import BaseModel, Field, ConfigDict, HttpUrl, FilePath
from tools.faker import fake
from config import settings


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
    upload_file: FilePath

class CreateFileResponseSchema(BaseModel):
    """
    Описание структуры ответа создания файла.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Описание структуры ответа получения файла.
    """
    file: FileSchema