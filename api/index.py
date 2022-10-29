from flask import Flask
from flask_cors import CORS
from dotenv import dotenv_values

from api.db.models import db
from api.routes.index import get_routes

ENV = dotenv_values()

api = Flask(__name__)
CORS(api)

if ENV["ENVIRONMENT"] == "development":
    api.config.from_object("config.DevConfig")

    db.init_app(api)

    with api.app_context():
        db.create_all()

else:
    api.config.from_object("config.ProdConfig")

get_routes(api)

if __name__ == "__main__":
    debug = api.config["DEBUG"]
    port = api.config["PORT"]

    api.run(debug=debug, port=port)
