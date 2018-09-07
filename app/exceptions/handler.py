from flask import Blueprint
from app.exceptions.systemexceptions import *
"""
Managing the error in different app and routes
Flask have capability of managing blueprint and the routes
All exceptions are loaded here
"""

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(UniqueConstraintException)
def handle_unique_constraint(error):
    return error.to_dict()
