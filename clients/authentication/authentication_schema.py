from pydantic import BaseModel, Field
from tools.fakers import fake

"""
Используем Field(alias="..."). Так как в API могут использоваться поля в camelCase, 
но в Python принят snake_case, мы добавили alias через Field(), чтобы сохранить совместимость
 """
#Field для альясов
class TokenSchema(BaseModel): # Наследуем от BaseModel вместо TypedDict
    """
        Описание структуры аутентификационных токенов.
    """
    token_type: str = Field(alias = "tokenType")
    access_token: str = Field(alias = "accessToken")
    refresh_token: str = Field(alias = "refreshToken")


class LoginRequestSchema(BaseModel): # Наследуем от BaseModel вместо TypedDict
    """
        Описание структуры запроса на аутентификацию.
    """
    email: str = Field(default_factory=fake.email)
    password: str = Field(default_factory=fake.password)


class LoginResponseSchema(BaseModel):  # Наследуем от BaseModel
    """
        Описание структуры ответа аутентификации.
    """
    token: TokenSchema


class RefreshRequestSchema(BaseModel): # Наследуем от BaseModel
    """
        Описание структуры запроса для обновления токена.
    """
    refresh_token: str = Field(alias = "refreshToken", default_factory=fake.sentence) # Использовали alise

