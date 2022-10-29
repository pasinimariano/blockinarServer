import jwt
from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error


def token_validator(api):
    def decorator(func):
        @wraps(func)
        def token_required():
            secret_key = api.config.get("SECRET_KEY")
            token = request.headers.get('token')
            if not token or token is None:
                return send_invalid_error("Token is missing")

            try:
                jwt.decode(token, secret_key, algorithms=["HS256"])

            except jwt.ExpiredSignatureError:
                return send_invalid_error("Token is expired")

            except jwt.InvalidTokenError:
                return send_invalid_error("Token is invalid")

            return func()
        return token_required
    return decorator
