from flask import Blueprint, jsonify, request

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.validators.events_creator_validator import events_creator_validator

event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_event():
    events_creator_validator(request)

    req = HttpRequest(body=request.json)
    res = HttpResponse(body={"Events": "Hello World!"}, status_code=201)

    return jsonify(res.body), res.status_code