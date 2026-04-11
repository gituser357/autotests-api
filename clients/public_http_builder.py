from httpx import Client

def get_public_http_client() -> Client:
    """
            Функция создаёт экземпляр httpx.Client с базовыми настройками.
            Далее с помощью этой функции, инициализируем клиенты:
               client=get_public_http_client()

            :return: Готовый к использованию объект httpx.Client.
    """
    return Client(timeout=100, base_url="http://localhost:8000")