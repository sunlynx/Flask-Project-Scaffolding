from flask import Flask
from config.initializer import config
from routes.initializer import router
from database.initializer import db, migrate
from flask import render_template
import os

"""
create all initialization of app here.
To change the configuration quickly
"""

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV')])
router.init_app(app)
db.init_app(app)
migrate.init_app(app)


@app.route('/')
def hello_world():
    """
    return welcome page when access route page with get requests
    :return:
    """
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
