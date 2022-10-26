from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from api.db.models import admin, bookings, rooms, categories, status
from api.routes.index import get_routes

api = Flask(__name__)
CORS(api)

api.config.from_object("config.DevConfig")

db = SQLAlchemy(api)

AdminModel = admin(db)
BookingsModel = bookings(db)
RoomsModel = rooms(db)
CategoriesModel = categories(db)
StatusModel = status(db)

get_routes(api, db, AdminModel, CategoriesModel, StatusModel)
"""
with api.app_context():
    db.create_all()
    
"""
if __name__ == "__main__":
    debug = api.config["DEBUG"]
    port = api.config["PORT"]

    api.run(debug=debug, port=port)
