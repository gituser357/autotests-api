# Этот файл будет содержать тест-кейсы, проверяющие функциональность API по работе с файлами.

from http import HTTPStatus

import pytest

from clients.files.files_client import FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response
from tools.assertions.schema import validate_json_schema


# тест, который проверяет создание файла через API.

@pytest.mark.files # зарегистрировал ее в pytest.ini, чтобы можно было фильтровать тесты по меткам
@pytest.mark.regression
class TestFiles:
    def test_create_file(self, files_client: FilesClient):
        request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")

        response = files_client.create_file_api(request)
        response_data = CreateFileResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_file_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

"""
Тест test_create_file выполняет следующие проверки:

1. Формирует запрос на создание файла
Создаем объект CreateFileRequestSchema, указывая путь к файлу ./testdata/files/image.png.
Это файл, который будет отправляться на сервер.

2. Отправляет запрос к API
Используем files_client.create_file_api(request), чтобы отправить запрос.
Получаем response, который содержит HTTP-ответ сервера.

3. Десериализует JSON-ответ
Так как сервер возвращает JSON-ответ, преобразуем его в CreateFileResponseSchema.
Для этого используем метод model_validate_json(response.text), который парсит JSON в объект Pydantic.

4.Проверяет статус-код
Используем assert_status_code(response.status_code, HTTPStatus.OK), чтобы убедиться, что сервер вернул 200 OK.
Если API вернул ошибку, тест сразу упадет.

5. Проверяет корректность данных в ответе
Вызываем assert_create_file_response(request, response_data), которая проверяет, что:
Имя файла в ответе совпадает с тем, что передавали.
Директория соответствует отправленному значению.
URL файла сформирован корректно.

6.Проверяет соответствие JSON-схеме
validate_json_schema(response.json(), response_data.model_json_schema()) проверяет, что JSON-ответ API соответствует ожидаемой схеме, заданной в CreateFileResponseSchema.
Это помогает убедиться, что API не изменило структуру ответа.
"""