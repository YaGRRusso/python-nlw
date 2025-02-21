from src.model.configs.connection import DBConnectionHandler
from src.model.entities.subscribers import Inscritos

class SubscribersRepository:
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
    
    def select_subscriber(self, subscriber_email) -> Inscritos:
        with DBConnectionHandler() as db:
            return (
                db.session
                .query(Inscritos)
                .filter(Inscritos.email == subscriber_email)
                .one_or_none()
            )
            