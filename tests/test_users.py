# В этом файле мы будем хранить автотесты, связанные с API пользователей /api/v1/users:
# (создание, получение, обновление, удаление).

from http import HTTPStatus
import pytest
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
# Импортируем функцию для проверки ответа создания юзера
from tools.assertions.users import assert_create_user_response

@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client: PublicUsersClient): # передали фикстуру в аргументы

    request = CreateUserRequestSchema() # создаем пользователя
    response = public_users_client.create_user_api(request) # получаем ответ
    response_data = CreateUserResponseSchema.model_validate_json(response.text) # валидируем данные

    assert_status_code(response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа создания юзера
    assert_create_user_response(request, response_data)

    validate_json_schema(response.json(), response_data.model_json_schema()) # Валидируем json схему
