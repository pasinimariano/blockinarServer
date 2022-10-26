from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.services.CategoriesService import CategoriesService


def get_all_categories_controller(api, db, categories_model, marshmallow):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    service = CategoriesService(db, categories_model)

                    all_categories = service.get_all_categories()

                    if all_categories["ok"] is False:
                        return send_invalid_error(all_categories["error"])

                    serialized_categories = marshmallow.dump(all_categories["categories"])

                    return func(serialized_categories)
                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def create_category_controller(api, db, categories_model):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    category_name, price = req["category_name"], req["price"]

                    service = CategoriesService(db, categories_model, category_name, price)

                    new_category = service.create_new_category()

                    if new_category["ok"] is False:
                        return send_invalid_error(new_category["error"])

                    return func(new_category["msg"])

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator

