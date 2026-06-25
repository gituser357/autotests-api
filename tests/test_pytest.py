def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():# Новый тест, которые проверяет положительный кейс
    x = 5
    assert x == 6 # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка