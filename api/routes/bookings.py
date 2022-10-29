from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.bookings_schemas import create_booking_schema
from api.controllers.bookings_controllers import get_all_rooms_controller, \
    create_booking_controller


def bookings_routes(api):
    @api.route("/bookings", methods=["GET"])
    @token_validator()
    @get_all_rooms_controller(api)
    def get_all_bookings(response):
        return make_response(
            response,
            200
        )

    @api.route("/bookings/create", methods=["POST"])
    @token_validator()
    @data_validator(create_booking_schema)
    @create_booking_controller(api)
    def create_booking(response):
        return make_response(
            response,
            200
        )
