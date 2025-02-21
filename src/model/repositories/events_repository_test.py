import pytest
from .events_repository import EventsRepository

@pytest.mark.skip(reason='Insert in DB')
def test_insert_eventos():
    repository = EventsRepository()
    repository.insert('Test Event')

@pytest.mark.skip(reason='Select in DB')
def test_select_eventos():
    repository = EventsRepository()
    event = repository.select('Test Event')
    assert event.nome == 'Test Event'