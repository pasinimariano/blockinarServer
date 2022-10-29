from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.utils.hash_password import hash_password, check_password
from api.utils.token_generator import token_generator
from api.services.AdminService import AdminService


def create_admin_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    first_name, last_name, email = req["first_name"], req["last_name"], req["email"]
                    password, role = req["password"], req["role"]

                    hashed_password = hash_password(password)

                    service = AdminService(email, hashed_password, first_name, last_name, role)

                    new_admin = service.create_new_admin()

                    if new_admin["ok"] is False:
                        return send_invalid_error(new_admin["error"])

                    return func(new_admin["msg"])

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def login_admin_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    email, password = req["email"], req["password"]

                    service = AdminService(email)

                    res = service.get_admin_by_email()

                    if res["ok"] is False:
                        return send_invalid_error(res["error"])

                    password_validator = check_password(password, res["admin"].password)

                    if password_validator is False:
                        return send_invalid_error("Incorrect password")

                    token = token_generator(email, api)

                    if token["ok"] is False:
                        return send_invalid_error(token["error"])

                    return func({"token": token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator
