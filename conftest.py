#подключаем pytest плагины
#теперь фикстуры глобально доступны по всем папкам


pytest_plugins = (
    "fixtures.users",
    "fixtures.authentication"
)