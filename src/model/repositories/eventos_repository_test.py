import pytest
from .eventos_repository import EventosRepository

@pytest.mark.skip(reason='Insert in DB')
def test_insert_eventos():
    repository = EventosRepository()
    repository.insert('Test Event')

@pytest.mark.skip(reason='Select in DB')
def test_select_eventos():
    repository = EventosRepository()
    event = repository.select_event('Test Event')
    assert event.nome == 'Test Event'