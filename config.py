import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_POOL_RECYCLE = os.environ.get("SQLALCHEMY_POOL_RECYCLE")
    ENVIRONMENT = os.environ.get("ENVIRONMENT")


class ProdConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
