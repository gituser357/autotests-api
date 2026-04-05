from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class GetExercisesQueryDict(TypedDict):
    """
           Описание структуры запроса на получение списка упражнений.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
               Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str
    estimatedTime: str | None

class UpdateExercisesRequestDict(TypedDict):
    """
               Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
            Клиент для работы с /api/v1/exercises
    """

    def get_exercises(self, query: GetExercisesQueryDict) -> Response:
        """
                        Метод получения списка упражнений.

                        :param query: Словарь из courseId.
                        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)

    def get_exercise(self, exercise_id:str)->Response:
        """
                        Метод получения упражнения.

                        :param exercise_id: Идентификатор упражнения.
                        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise(self, request: CreateExerciseRequestDict):
        """
                        Метод создания упражнения.

                        :param request: Словарь из CreateExercisesRequestDict
                        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request)

    def update_exercise(self, exercise_id:str, request: UpdateExercisesRequestDict) -> Response:
        """
                        Метод обновления упражнения.
                        :param exercise_id: Идентификатор упражнения.
                        :param request: Словарь из CreateExercisesRequestDict
                        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise(self, exercise_id:str)->Response:
        """
                        Метод удаления упражнения.

                        :param exercise_id: Идентификатор упражнения.
                        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")