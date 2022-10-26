import jwt
from flask import request
from functools import wraps
from dotenv import dotenv_values

from api.utils.send_errors import send_invalid_error

ENV = dotenv_values()
SECRET_KEY = ENV["SECRET_KEY"]


def token_validator():
    def decorator(func):
        @wraps(func)
        def token_required():
            token = request.headers.get('token')
            if not token or token is None:
                return send_invalid_error("Token is missing")

            try:
                jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

            except jwt.ExpiredSignatureError:
                return send_invalid_error("Token is expired")

            except jwt.InvalidTokenError:
                return send_invalid_error("Token is invalid")

            return func()
        return token_required
    return decorator
