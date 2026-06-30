#  здесь объявляются фикстуры

import pytest
from pydantic import BaseModel, EmailStr
# Импортируем API клиенты
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    # свойство
    @property
    def email(self)-> EmailStr: # Быстрый доступ к email пользователя
        return self.request.email

    # свойство
    @property
    def password(self) -> str: # Быстрый доступ к password пользователя
        return self.request.password

@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> PublicUsersClient:  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()

# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture: # с вложенной фикстурой public_users_client в аргументах
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request, response=response) # Возвращаем все нужные данные
