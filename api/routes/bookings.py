from flask import make_response, jsonify


def bookings_routes(api):
    @api.route("/bookings", methods=["GET"])
    def get_all_bookings(response):
        return make_response(
            jsonify(response),
            200
        )
