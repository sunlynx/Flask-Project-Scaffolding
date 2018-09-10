from flask import Flask
from config.initializer import config
from database.initializer import db, migrate, ma
from app.exceptions.handler import errors
from routes.api import router
from flask import render_template
import os, operator

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


@app.route('/')
def home_page():
    """
    return welcome page when access route page with get requests
    :return:
    """
    return render_template('welcome.html')


@app.cli.command()
def routes():
    rules = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))

    sort_by_rule = operator.itemgetter(2)
    for endpoint, methods, rule in sorted(rules, key=sort_by_rule):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)


if __name__ == '__main__':
    app.run()
