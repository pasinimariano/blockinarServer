import jwt
from datetime import datetime, timedelta
from dotenv import dotenv_values


def token_generator(email, api):
    try:
        secret_key = api.config.get("SECRET_KEY")
        payload = {
            "exp": datetime.utcnow() + timedelta(minutes=40),
            "iat": datetime.utcnow(),
            "sub": email
        }

        token = jwt.encode(
            payload,
            secret_key,
            algorithm="HS256"
        )

        return {"ok": True, "token": token}

    except Exception as error:
        return {"ok": False, "error": error}


def token_decode(token):
    decoded_token = jwt.decode(token, options={"verify_signature": False})

    return decoded_token["sub"]
