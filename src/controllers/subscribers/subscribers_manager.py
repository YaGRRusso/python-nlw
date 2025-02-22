from src.model.repositories.interfaces.subscribers_repository import SubscribersRepositoryInterface

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse

class SubscribersManager:
    def __init__(self, subscribers_repo: SubscribersRepositoryInterface):
        self.__subscribers_repo = subscribers_repo

    def get_subscribers_by_link(self, http_request: HttpRequest) -> HttpResponse:
        param_link = http_request.param['link']
        param_event_id = http_request.param['event_id']

        subscribers = self.__subscribers_repo.select_by_link(param_link, param_event_id)
        return self.__format_subs_by_link(subscribers)

    def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
        param_event_id = http_request.param['event_id']

        event_ranking = self.__subscribers_repo.get_ranking(param_event_id)
        return self.__format_event_ranking(event_ranking)

    def __format_subs_by_link(self, subscribers: list) -> HttpResponse:
        formatted_subscriber = []

        for sub in subscribers:
            formatted_subscriber.append(
                {
                    "nome": sub.nome,
                    "email": sub.email,
                }
            )
            
        return HttpResponse(
            body={
                "data": {
                    "Type": "Subscriber",
                    "count": len(formatted_subscriber),
                    "subscribers": formatted_subscriber
                }
            },
            status_code=200
        )

    def __format_event_ranking(self, event_ranking: list) -> HttpResponse:
        formatted_event_ranking = []

        for position in event_ranking:
            formatted_event_ranking.append(
                {
                    "link": position.link,
                    "total_subscribers": position.total,
                }
            )
            
        return HttpResponse(
            body={
                "data": {
                    "Type": "Ranking",
                    "count": len(formatted_event_ranking),
                    "ranking": formatted_event_ranking
                }
            },
            status_code=200
        )