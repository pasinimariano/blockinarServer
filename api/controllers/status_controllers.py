from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.utils.token_generator import token_decode, token_generator
from api.services.StatusService import StatusService
from api.db.marshmallows import StatusSchema

marshmallow = StatusSchema(many=True)


def get_all_status_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    service = StatusService()
                    token = request.headers.get('token')
                    email = token_decode(token)

                    all_status = service.get_all_status()

                    if all_status["ok"] is False:
                        return send_invalid_error(all_status["error"])

                    serialized_categories = marshmallow.dump(all_status["status"])
                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"status": serialized_categories, "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def create_status_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    booking_status = req["booking_status"]
                    service = StatusService(booking_status=booking_status)
                    token = request.headers.get('token')
                    email = token_decode(token)

                    new_status = service.create_new_status()

                    if new_status["ok"] is False:
                        return send_invalid_error(new_status["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def update_status_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    status_id = request.args.get("id")
                    req = request.json
                    booking_status = req["booking_status"]
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = StatusService(status_id, booking_status)

                    update_status = service.update_status()

                    if update_status["ok"] is False:
                        return send_invalid_error(update_status["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def delete_status_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    status_id = request.args.get("id")
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = StatusService(status_id)

                    delete_status = service.delete_status()

                    if delete_status["ok"] is False:
                        return send_invalid_error(delete_status["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator
