from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.utils.token_generator import token_decode, token_generator
from api.services.CategoriesService import CategoriesService
from api.db.marshmallows import CategoriesSchema

marshmallow = CategoriesSchema(many=True)


def get_all_categories_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    service = CategoriesService()
                    token = request.headers.get('token')
                    email = token_decode(token)

                    all_categories = service.get_all_categories()

                    if all_categories["ok"] is False:
                        return send_invalid_error(all_categories["error"])

                    serialized_categories = marshmallow.dump(all_categories["categories"])
                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"categories": serialized_categories, "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def create_category_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    category_name, price = req["category_name"], req["price"]
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = CategoriesService(category_name=category_name, price=price)

                    new_category = service.create_new_category()

                    if new_category["ok"] is False:
                        return send_invalid_error(new_category["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def update_category_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    category_id = request.args.get("id")
                    req = request.json
                    category_name, price = req["category_name"], req["price"]
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = CategoriesService(category_id, category_name, price)

                    update_category = service.update_category()

                    if update_category["ok"] is False:
                        return send_invalid_error(update_category["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def delete_category_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    category_id = request.args.get("id")
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = CategoriesService(category_id)

                    delete_category = service.delete_category()

                    if delete_category["ok"] is False:
                        return send_invalid_error(delete_category["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator
