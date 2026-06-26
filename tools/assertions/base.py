# в этом файле хранятся все базовые проверки, инкапсулируя логику
# если вносить изменения то только в одном файле - здесь, а не во всех тестах

from typing import Any


def assert_status_code(actual: int, expected: int):
    """
        Проверяет, что фактический статус-код ответа соответствует ожидаемому.

        :param actual: Фактический статус-код ответа.
        :param expected: Ожидаемый статус-код.
        :raises AssertionError: Если статус-коды не совпадают.
    """
    assert actual == expected, (
        'Некорректный статус-код. '
        f'Ожидаемый статус-код {expected}. '
        f'Фактический статус-код {actual}. '
    )

def assert_equal(actual: Any, expected: Any, name: str):
    """
        Проверяет, что фактическое значение равно ожидаемому.

        :param name: Название проверяемого значения.
        :param actual: Фактическое значение.
        :param expected: Ожидаемое значение.
        :raises AssertionError: Если фактическое значение не равно ожидаемому.
    """
    assert actual == expected, (
        f'Некорректное значение: "{name}". '
        f'Ожидаемое значение: {expected}. '
        f'Фактическое значение: {actual}. '
    )

def assert_is_true(actual: Any, name: str):
    """
    Проверяет, что фактическое значение является истинным.
    Для проверки непустых значений

    :param name: Название проверяемого значения.
    :param actual: Фактическое значение.
    :raises AssertionError: Если фактическое значение ложно.
    """
    assert actual, (
        f'Некорректное значение: "{name}". '
        f'Фактическое значение: {actual}'
    )