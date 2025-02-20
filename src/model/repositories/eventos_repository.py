from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events import Eventos

class EventosRepository:
    def insert(self, event_name: str) -> None:
        with DBConnectionHandler() as db:
            try:
                new_event = Eventos(nome=event_name)
                db.session.add(new_event)
                db.session.commit()
            except Exception as exc:
                db.session.rollback()
                raise exc
            
    def select_event(self, event_name) -> Eventos:
        with DBConnectionHandler() as db:
            return (
                db.session
                .query(Eventos)
                .filter(Eventos.nome == event_name)
                .one_or_none()
            )