from sqlalchemy import func, desc

from src.model.configs.connection import DBConnectionHandler
from src.model.entities.subscribers import Inscritos

from .interfaces.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
    def insert(self, subscriber_infos: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos(
                    nome=subscriber_infos['nome'],
                    email=subscriber_infos['email'],
                    link=subscriber_infos.get('link'),
                    evento_id=subscriber_infos['evento_id']
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exc:
                db.session.rollback()
                raise exc
    
    def select(self, subscriber_email) -> Inscritos:
        with DBConnectionHandler() as db:
            return (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == subscriber_email)
                .one_or_none()
            )
        
    def select_by_link(self, link: str, event_id: int) -> list:
        with DBConnectionHandler() as db:
            data = (
                db.session
                .query(Inscritos)
                .filter(
                    Inscritos.link == link,
                    Inscritos.evento_id == event_id
                )
                .all()
            )
            return data

    def get_ranking(self, event_id: int) -> list:
        with DBConnectionHandler() as db:
            result = (
                db.session
                .query(
                    Inscritos.link,
                    func.count(Inscritos.id).label("total")
                )
                .filter(
                    Inscritos.evento_id == event_id,
                    Inscritos.link.isnot(None)
                )
                .group_by(Inscritos.link)
                .order_by(desc("total"))
                .all()
            )
            return result
            