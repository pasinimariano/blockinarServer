from flask import make_response, jsonify

from api.middlewares.data_validator import data_validator
from api.schemas.create_admin_schema import create_admin_schema
from api.controllers.admins_controllers import create_admin_controller


def admins_routes(api, admin_model, db):
    @api.route("/admin/create", methods=["POST"])
    @data_validator(create_admin_schema)
    @create_admin_controller(api, admin_model, db)
    def create_admin(response):
        return make_response(
            response,
            200
        )
