from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.status_schemas import create_status_schema
from api.controllers.status_controllers import get_all_status_controller,\
    create_status_controller, \
    update_status_controller, \
    delete_status_controller


def status_routes(api, db, status_model, marshmallow):
    @api.route("/status", methods=["GET"])
    @token_validator()
    @get_all_status_controller(api, db, status_model, marshmallow)
    def get_all_status(response):
        return make_response(
            response,
            200
        )

    @api.route("/status/create", methods=["POST"])
    @token_validator()
    @data_validator(create_status_schema)
    @create_status_controller(api, db, status_model)
    def create_status(response):
        return make_response(
            response,
            200
        )

    @api.route("/status/update", methods=["PUT"])
    @data_validator(create_status_schema)
    @token_validator()
    @update_status_controller(api, db, status_model)
    def update_status(response):
        return make_response(
            response,
            200
        )

    @api.route("/status/delete", methods=["DELETE"])
    @token_validator()
    @delete_status_controller(api, db, status_model)
    def delete_status(response):
        return make_response(
            response,
            200
        )
