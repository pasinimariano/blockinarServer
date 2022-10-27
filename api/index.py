from flask import Flask
from flask_cors import CORS

from api.db.models import db
from api.routes.index import get_routes

api = Flask(__name__)
CORS(api)

api.config.from_object("config.DevConfig")

db.init_app(api)

get_routes(api)

with api.app_context():
    db.create_all()

if __name__ == "__main__":
    debug = api.config["DEBUG"]
    port = api.config["PORT"]

    api.run(debug=debug, port=port)
