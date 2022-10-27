from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.rooms_schema import create_room_schema
from api.controllers.rooms_controllers import get_all_rooms_controller,\
    create_room_controller, \
    update_room_controller, \
    delete_room_controller


def rooms_routes(api):
    @api.route("/rooms", methods=["GET"])
    @token_validator()
    @get_all_rooms_controller(api)
    def get_all_rooms(response):
        return make_response(
            response,
            200
        )

    @api.route("/rooms/create", methods=["POST"])
    @token_validator()
    @data_validator(create_room_schema)
    @create_room_controller(api)
    def create_room(response):
        return make_response(
            response,
            200
        )

    @api.route("/rooms/update", methods=["PUT"])
    @token_validator()
    @data_validator(create_room_schema)
    @update_room_controller(api)
    def update_room(response):
        return make_response(
            response,
            200
        )

    @api.route("/rooms/delete", methods=["DELETE"])
    @token_validator()
    @delete_room_controller(api)
    def delete_room(response):
        return make_response(
            response,
            200
        )
