from flask_dotenv import DotEnv
import os


class Initializer:

    """
    Initializer loads the env file and configures the flask environment
    whereas .flaskenv is loaded automatically. you need not to perform action on it
    Other specific initializer will override the properties they need
    """
    SECRET_KEY = '6ccb843acd9231bcd411aac7f9b6b453718fb0d978b0b3136865ab578448491d'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DB_URI')

    def __init__(self):
        pass

    @classmethod
    def init_app(cls, app):
        env = DotEnv()
        env.init_app(app)


class ProductionInitializer(Initializer):
    DEBUG = True


class DevelopmentInitializer(Initializer):
    DEBUG = True


class StagingInitializer(Initializer):
    DEBUG = True


config = {
    'development': DevelopmentInitializer,
    'production': ProductionInitializer,
    'staging': StagingInitializer
}
