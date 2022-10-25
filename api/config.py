from os import environ
from dotenv import dotenv_values

ENV = dotenv_values()


class Config:
    SECRET_KEY = ENV["SECRET_KEY"]
    "especificar el domaing de cookie"
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    SQLALCHEMY_DATABASE_URI = ENV["SQLALCHEMY_DATABASE_URI"]


class ProdConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    PORT = 3004
