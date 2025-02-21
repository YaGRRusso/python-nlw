from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.validators.events_creator_validator import events_creator_validator

from src.controllers.events.events_creator import EventsCreator
from src.model.repositories.events_repository import EventsRepository

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_event():
    events_creator_validator(request)

    event_repo = EventsRepository()
    events_creator = EventsCreator(event_repo)

    req = HttpRequest(body=request.json)
    res = events_creator.create(req)

    return jsonify(res.body), res.status_code