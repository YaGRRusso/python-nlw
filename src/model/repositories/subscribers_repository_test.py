import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip(reason='Insert in DB')
def test_insert_inscritos():
    repository = SubscribersRepository()
    repository.insert({
        "nome": "Subscriber Test",
        "email": "email@email.com",
        "evento_id": 1
    })

@pytest.mark.skip(reason='Select in DB')
def test_select_inscritos():
    repository = SubscribersRepository()
    subscriber = repository.select("email@email.com")
    assert subscriber.nome == "Subscriber Test"