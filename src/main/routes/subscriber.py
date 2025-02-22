from flask import Blueprint, jsonify, request

from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

from src.controllers.subscribers.subscribers_creator import SubscribersCreator
from src.controllers.subscribers.subscribers_manager import SubscribersManager

from src.model.repositories.subscribers_repository import SubscribersRepository

subscriber_route_bp = Blueprint('subscriber_route', __name__)

@subscriber_route_bp.route('/subscriber', methods=['POST'])
def create_subscriber():
    subscribers_creator_validator(request)

    subscribers_repo = SubscribersRepository()
    subscribers_creator = SubscribersCreator(subscribers_repo)

    req = HttpRequest(body=request.json)
    res = subscribers_creator.create(req)

    return jsonify(res.body), res.status_code

@subscriber_route_bp.route("/subscriber/link/<link>/event/<event_id>", methods=["GET"])
def subscribers_by_link(link, event_id):
    subscribers_repo = SubscribersRepository()
    subs_manager = SubscribersManager(subscribers_repo)

    req = HttpRequest(param={ "link": link, "event_id": event_id })
    res = subs_manager.get_subscribers_by_link(req)

    return jsonify(res.body), res.status_code

@subscriber_route_bp.route("/subscriber/ranking/event/<event_id>", methods=["GET"])
def link_ranking(event_id):
    subscribers_repo = SubscribersRepository()
    subs_manager = SubscribersManager(subscribers_repo)

    req = HttpRequest(param={ "event_id": event_id })
    res = subs_manager.get_event_ranking(req)

    return jsonify(res.body), res.status_code