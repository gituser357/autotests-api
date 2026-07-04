# вспомогательная функция, которая проверяет корректность ответа API на создание файла
# 9.2


from clients.files.files_schema import CreateFileResponseSchema, CreateFileRequestSchema
from tools.assertions.base import assert_equal


def assert_create_file_response(request: CreateFileRequestSchema, response: CreateFileResponseSchema):
    """
    Проверяет, что ответ на создание файла соответствует запросу.

    :param request: Исходный запрос на создание файла.
    :param response: Ответ API с данными файла.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    # Формируем ожидаемую ссылку на загруженный файл
    expected_url = f"http://localhost:8000/static/{request.directory}/{request.filename}"

    assert_equal(str(response.file.url), expected_url, "url") # Для корректного сравнения приводим HttpUrl к строке
    assert_equal(response.file.filename, request.filename, "filename") #
    assert_equal(response.file.directory, request.directory, "directory")

# можно дополнительно выполнить GET-запрос на expected_url.
# убедиться, что не только API вернул правильную ссылку, но и сам файл действительно загружен и доступен