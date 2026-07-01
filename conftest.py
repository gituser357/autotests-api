#подключаем pytest плагины
#теперь фикстуры глобально доступны по всем папкам


pytest_plugins = (
    "fixtures.users",
    "fixtures.files",
    "fixtures.courses",  # Добавляем фикстуры для работы с курсами
    "fixtures.authentication"
)