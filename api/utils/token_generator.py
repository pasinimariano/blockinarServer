import jwt
from datetime import datetime, timedelta
from dotenv import dotenv_values

ENV = dotenv_values()
SECRET_KEY = ENV["SECRET_KEY"]


def token_generator(email):
    try:
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=40),
            "iat": datetime.utcnow(),
            "sub": email
        }

        token = jwt.encode(
            payload,
            SECRET_KEY,
            algorithm="HS256"
        )

        return {"ok": True, "token": token}

    except Exception as error:
        return {"ok": False, "error": error}


def token_decode(token):
    decoded_token = jwt.decode(token, options={"verify_signature": False})

    return decoded_token["sub"]
