from pydantic import BaseModel, HttpUrl


class FileSchema(BaseModel): #взяли из response GET
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl


class CreateFileRequestSchema(BaseModel):
    """
        Описание структуры запроса на создание файла.
    """
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseSchema(BaseModel):
    """
        Описание структуры запроса на создание файла.
    """
    file: FileSchema