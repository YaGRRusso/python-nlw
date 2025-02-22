import pytest
from .events_link_repository import EventsLinkRepository

@pytest.mark.skip(reason='Insert in DB')
def test_insert_eventos_link():
    repository = EventsLinkRepository()
    repository.insert(1, 1)