from flask_marshmallow import Marshmallow

from api.routes.admins import admins_routes
from api.routes.categories import categories_routes
from api.db.marshmallow import set_categories_schema


def get_routes(api, db, admin_model, categories_model):
    marshmallow = Marshmallow(api)

    get_categories_schema = set_categories_schema(marshmallow, categories_model, many=True)

    admins_routes(api, db, admin_model)
    categories_routes(api, db, categories_model, get_categories_schema)
