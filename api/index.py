from flask import Flask
from flask_cors import CORS

from api.db.models import db
from api.routes.index import get_routes


api = Flask(__name__)
CORS(api)

api.config.from_object("config.DevConfig")

if api.config.get("ENVIRONMENT") == "development":
    db.init_app(api)

    with api.app_context():
        db.create_all()

else:
    api.config.from_object("config.ProdConfig")

get_routes(api)

