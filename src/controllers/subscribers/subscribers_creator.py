from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersCreator:
    def __init__(self, subscriber_repo: SubscribersRepositoryInterface):
        self.__subscriber_repo = subscriber_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body["data"]

        self.__validate(body["email"])
        self.__insert(body)

        return self.__format_response(body)
    
    def __validate(self, email: str) -> None:
        response = self.__subscriber_repo.select(email)
        if response: raise Exception('Subscriber already exists')

    def __insert(self, subscriber_infos: dict) -> None:
        self.__subscriber_repo.insert(subscriber_infos)

    def __format_response(self, subscriber_infos: dict) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Subscriber",
                    "count": 1,
                    "attributes": subscriber_infos
                }
            },
            status_code=201
        )