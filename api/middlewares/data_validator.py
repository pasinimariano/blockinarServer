from cerberus import Validator
from functools import wraps
from flask import request

from api.utils.send_errors import send_invalid_error


def data_validator(schema):
    def decorator(func):
        @wraps(func)
        def wrapper():
            validator = Validator()
            req = request.json
            res = validator.validate(req, schema)

            if res is False:
                return send_invalid_error(validator.errors)

            return func()
        return wrapper
    return decorator
