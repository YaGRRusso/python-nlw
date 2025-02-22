import random

from src.model.configs.connection import DBConnectionHandler
from src.model.entities.events_link import EventosLink

class EventsLinkRepository():
    def insert(self, event_id: int, subscriber_id: int) -> str:
        with DBConnectionHandler() as db:
            try:
                link_hash = "".join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
                link_format = f'event-{event_id}-{subscriber_id}-{link_hash}'

                new_event_link = EventosLink(
                    evento_id=event_id,
                    inscrito_id=subscriber_id,
                    link=link_format
                )
                db.session.add(new_event_link)
                db.session.commit()

                return link_format
            except Exception as exc:
                db.session.rollback()
                raise exc
            
    def select(self, event_id: int, subscriber_id: int) -> EventosLink:
        with DBConnectionHandler() as db:
            return (
                db.session
                .query(EventosLink)
                .filter(
                    EventosLink.evento_id == event_id,
                    EventosLink.inscrito_id == subscriber_id
                )
                .one_or_none()
            )