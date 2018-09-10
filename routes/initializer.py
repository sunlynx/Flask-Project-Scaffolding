from flask_restful import Api
from flask import Blueprint

"""
This file handles the routes.
This helps to load the configuration of the router
"""
router = Api(prefix='/v1')
errors = Blueprint('errors', __name__)
