from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.categories_schemas import create_category_schema
from api.controllers.rooms_controllers import get_all_rooms_controller,\
    create_room_controller


def rooms_routes(api, db, rooms_model, marshmallow):
    @api.route("/rooms", methods=["GET"])
    @token_validator()
    @get_all_rooms_controller(api, db, rooms_model, marshmallow)
    def get_all_rooms(response):
        return make_response(
            response,
            200
        )

    @api.route("/rooms/create", methods=["POST"])
    @create_room_controller(api, db, rooms_model)
    def create_room(response):
        return make_response(
            response,
            200
        )

