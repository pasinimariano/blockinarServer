from os import environ
from dotenv import dotenv_values

ENV = dotenv_values()


class Config:
    SECRET_KEY = ENV["SECRET_KEY"]
    SESSION_COOKIE_NAME = environ.get("SESSION_COOKIE_NAME")
    SQLALCHEMY_DATABASE_URI = ENV["SQLALCHEMY_DATABASE_URI"]
    ENVIRONMENT = ENV["ENVIRONMENT"]


class ProdConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
    PORT = 3001
