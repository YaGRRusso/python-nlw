from src.model.repositories.interfaces.events_link_repository import EventosLinkRepositoryInterface

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class EventsLinkCreator:
    def __init__(self, events_link_repo: EventosLinkRepositoryInterface):
        self.__events_link_repo = events_link_repo

    def create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body["data"]

        self.__check_event_link(body['event_id'], body['subscriber_id'])
        new_link = self.__create_event_link(body['event_id'], body['subscriber_id'])
        return self.__format_response(new_link, body['event_id'], body['subscriber_id'])

    def __check_event_link(self, event_id: int, subscriber_id: int) -> None:
        response = self.__events_link_repo.select(event_id, subscriber_id)
        if response: raise Exception("Link Already Exists!")

    def __create_event_link(self, event_id: int, subscriber_id: int) -> str:
        new_link = self.__events_link_repo.insert(event_id, subscriber_id)
        return new_link

    def __format_response(self, new_link: str, event_id: int, subscriber_id: int) -> HttpResponse:
        return HttpResponse(
            body={
                "data": {
                    "Type": "Event Link",
                    "count": 1,
                    "attributes": {
                        "link": new_link,
                        "event_id": event_id,
                        "subscriber_id": subscriber_id
                    }
                }
            },
            status_code=201
        )