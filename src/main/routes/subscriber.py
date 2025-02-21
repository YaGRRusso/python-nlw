from flask import Blueprint, jsonify, request

from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

from src.validators.subscribers_creator_validator import subscribers_creator_validator

subscriber_route_bp = Blueprint('subscriber_route', __name__)

@subscriber_route_bp.route('/subscriber', methods=['POST'])
def create_subscriber():
    subscribers_creator_validator(request)

    req = HttpRequest(body=request.json)
    res = HttpResponse(body={"Subscribers": "Hello World!"}, status_code=201)

    return jsonify(res.body), res.status_code