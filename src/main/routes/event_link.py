from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.controllers.events_link.events_link_creator import EventsLinkCreator
from src.model.repositories.events_link_repository import EventsLinkRepository

event_link_route_bp = Blueprint("event_link_route", __name__)

@event_link_route_bp.route("/event_link", methods=["POST"])
def create_new_link():
    events_link_repo = EventsLinkRepository()
    events_link_creator = EventsLinkCreator(events_link_repo)

    req = HttpRequest(body=request.json)
    res = events_link_creator.create(req)

    return jsonify(res.body), res.status_code