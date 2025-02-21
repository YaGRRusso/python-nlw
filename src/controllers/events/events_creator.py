from src.model.repositories.interfaces.events_repository import EventsRepositoryInterface

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsCreator:
    def __init__(self, event_repo: EventsRepositoryInterface):
        self.__event_repo = event_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body["data"]

        self.__validate(body["nome"])
        self.__insert(body["nome"])

        return self.__format_response(body["nome"])

    def __validate(self, event_name: str) -> None:
        response = self.__event_repo.select(event_name)
        if response: raise Exception('Event already exists')

    def __insert(self, event_name: str) -> None:
        self.__event_repo.insert(event_name)

    def __format_response(self, event_name: str) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "type": "Event",
                    "count": 1,
                    "attributes": {
                        "nome": event_name
                    }
                }
            },
            status_code=201
        )