from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.schemas.admin_schemas import create_admin_schema, login_admin_schema
from api.controllers.admins_controllers import create_admin_controller, login_admin_controller


def admins_routes(api, db, admin_model):
    @api.route("/admin/create", methods=["POST"])
    @data_validator(create_admin_schema)
    @create_admin_controller(api, admin_model, db)
    def create_admin(response):
        return make_response(
            response,
            200
        )

    @api.route("/admin/login", methods=["GET"])
    @data_validator(login_admin_schema)
    @login_admin_controller(api, db, admin_model)
    def login_admin(response):
        return make_response(
            response,
            200
        )

