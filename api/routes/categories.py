from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.middlewares.token_validator import token_validator
from api.schemas.categories_schemas import create_category_schema
from api.controllers.categories_controllers import get_all_categories_controller, create_category_controller


def categories_routes(api, db, categories_model, marshmallow):
    @api.route("/categories", methods=["GET"])
    @token_validator()
    @get_all_categories_controller(api, db, categories_model, marshmallow)
    def get_all_categories(response):
        return make_response(
            response,
            200
        )

    @api.route("/categories/create", methods=["POST"])
    @data_validator(create_category_schema)
    @token_validator()
    @create_category_controller(api, db, categories_model)
    def create_category(response):
        return make_response(
            response,
            200
        )
