from abc import ABC, abstractmethod
from src.model.entities.subscribers import Inscritos

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None: pass
    
    @abstractmethod
    def select(self, subscriber_email) -> Inscritos: pass

    @abstractmethod
    def select_by_link(self, link: str, event_id: int) -> list: pass

    @abstractmethod
    def get_ranking(self, event_id: int) -> list: pass
            