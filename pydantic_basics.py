"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""

from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel
import uuid


class FileSchema(BaseModel): # схема для вложенного объекта previewFile в json
    id: str
    url: HttpUrl
    filename: str
    directory: str

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field()
    def username(self)-> str:
        return f"{self.middle_name} {self.last_name}"

    def get_username(self) -> str:
        return f"{self.middle_name} {self.last_name}"


class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4())) #генерируем uuid если не присвоено значение
    title: str = "hi 1"
    max_score: int = Field(alias="maxScore", default=11) #default - прибиваем значение по умолчанию
    min_score: int = Field(alias="minScore", default=12)
    description: str = "hi 2"
    preview_file: FileSchema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime",default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

#классический способ иницализации модели
course_default_model = CourseSchema(
    id="course-id",
    title="Playwright",
    maxScore= 100,
    minScore=10,
    description="Playwright",
    previewFile = FileSchema(
        id="file-id",
        url="http://localhost:8080",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime= "1 week",
    createdByUser= UserSchema(
      id = "user-id",
      email = "user@gmail.com",
      lastName = "Bond",
      firstName = "Zara",
      middleName = "Alice"
    )
)
print(course_default_model)

#Выполнили десириализацию из словаря в модель
course_dict = {
    "id": "23",
    "title": "Playwright 2",
    "maxScore": 15,
    "minScore": 13,
    "description": "Playwright 5",
    "previewFile":{
        "id": "file-id",
        "url":"http://localhost:8080",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "7 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "A"
    }
}
course_dict_model= CourseSchema(**course_dict)
print(course_dict_model)


course_json = """
{
    "id": "course-id",
    "title": "Playwright 2",
    "maxScore": 15,
    "minScore": 13,
    "description": "Playwright 5",
    "previewFile":{
        "id": "file-id",
        "url":"http://localhost:8080",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "7 week",
    "createdByUser": {
        "id": "user-id",
        "email": "user@gmail.com",
        "lastName": "Bond",
        "firstName": "Zara",
        "middleName": "A"
    }
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print(course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))


user = UserSchema(
    id = "user-id",
    email = "1@gmail.com",
    lastName = "Bond",
    firstName = "Zara",
    middleName = "Alice"
)
print(user.get_username(), user.username)

try:
    file = FileSchema(
        id="file-id",
        url="httplocalhost:8080",
        filename="file.png",
        directory="courses",
    )
except ValidationError as error:
    print(error)
    print(error.errors())