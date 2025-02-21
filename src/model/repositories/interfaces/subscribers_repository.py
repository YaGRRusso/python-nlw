from abc import ABC, abstractmethod
from src.model.entities.subscribers import Inscritos

class SubscribersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, subscriber_infos: dict) -> None: pass
    
    @abstractmethod
    def select_subscriber(self, subscriber_email) -> Inscritos: pass
            