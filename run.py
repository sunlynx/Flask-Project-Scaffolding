from flask import Flask
from config.initializer import config
from database.initializer import db, migrate, ma
from app.exceptions.handler import errors
from routes.api import router
import os

"""
Initialization of blueprints and apps are done here only.
So, as to change the configuration quickly from one file
One of the reason is to avoid circular imports
"""

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV')])
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(errors)
router.init_app(app)
db.init_app(app)
ma.init_app(app)
migrate.init_app(app)


if __name__ == '__main__':
    app.run()
