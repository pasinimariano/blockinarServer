from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.categories_schemas import create_category_schema
from api.controllers.categories_controllers import get_all_categories_controller,\
    create_category_controller, \
    update_category_controller, \
    delete_category_controller


def categories_routes(api):
    @api.route("/categories", methods=["GET"])
    @token_validator(api)
    @get_all_categories_controller(api)
    def get_all_categories(response):
        return make_response(
            response,
            200
        )

    @api.route("/categories/create", methods=["POST"])
    @data_validator(create_category_schema)
    @token_validator(api)
    @create_category_controller(api)
    def create_category(response):
        return make_response(
            response,
            200
        )

    @api.route("/categories/update", methods=["PUT"])
    @data_validator(create_category_schema)
    @token_validator(api)
    @update_category_controller(api)
    def update_category(response):
        return make_response(
            response,
            200
        )

    @api.route("/categories/delete", methods=["DELETE"])
    @token_validator(api)
    @delete_category_controller(api)
    def delete_category(response):
        return make_response(
            response,
            200
        )
