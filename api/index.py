from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.db.models import bookings, rooms, categories, status
from api.db.marshmallow import set_bookings_schema, set_rooms_schema, set_categories_schema, set_status_schema

api = Flask(__name__)
CORS(api)

api.config.from_object("config.DevConfig")

db = SQLAlchemy(api)

BookingsModel = bookings(db)
RoomsModel = rooms(db)
CategoriesModel = categories(db)
StatusModel = status(db)

marshmallow = Marshmallow(api)

get_bookings_schema = set_bookings_schema(marshmallow, BookingsModel)
get_rooms_schema = set_rooms_schema(marshmallow, RoomsModel)
get_categories_schema = set_categories_schema(marshmallow, CategoriesModel)
get_status_schema = set_status_schema(marshmallow, StatusModel)


if __name__ == "__main__":
    debug = api.config["DEBUG"]
    port = api.config["PORT"]

    api.run(debug=debug, port=port)
