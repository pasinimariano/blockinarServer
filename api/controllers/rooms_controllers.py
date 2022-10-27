from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.utils.token_generator import token_decode, token_generator
from api.services.RoomsService import RoomsService
from api.db.marshmallows import RoomsSchema

marshmallow = RoomsSchema(many=True)


def get_all_rooms_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    service = RoomsService()
                    token = request.headers.get('token')
                    email = token_decode(token)

                    all_rooms = service.get_all_rooms()

                    if all_rooms["ok"] is False:
                        return send_invalid_error(all_rooms["error"])

                    serialized_rooms = marshmallow.dump(all_rooms["rooms"])
                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"rooms": serialized_rooms, "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def create_room_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    occupancy, max_occupancy, category_id = req["occupancy"], req["max_occupancy"], req["category_id"]
                    service = RoomsService(occupancy=occupancy, max_occupancy=max_occupancy, category_id=category_id)
                    token = request.headers.get('token')
                    email = token_decode(token)

                    new_room = service.create_new_room()

                    if new_room["ok"] is False:
                        return send_invalid_error(new_room["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def update_room_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    room_id = request.args.get("id")
                    req = request.json
                    occupancy, max_occupancy, category_id = req["occupancy"], req["max_occupancy"], req["category_id"]
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = RoomsService(room_id, occupancy, max_occupancy, category_id)

                    update_room = service.update_room()

                    if update_room["ok"] is False:
                        return send_invalid_error(update_room["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def delete_room_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    room_id = request.args.get("id")
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = RoomsService(room_id)

                    delete_room = service.delete_room()

                    if delete_room["ok"] is False:
                        return send_invalid_error(delete_room["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator




