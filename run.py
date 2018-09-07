from flask import Flask
from config.initializer import config
from database.initializer import db, migrate
from app.exceptions.handler import errors
from routes.api import *
import os

"""
create all initialization of app here.
To change the configuration quickly
"""

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV')])
app.register_blueprint(errors)
router.init_app(app)
db.init_app(app)
migrate.init_app(app)

if __name__ == '__main__':
    app.run()
