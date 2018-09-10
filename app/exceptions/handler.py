from app.exceptions.systemexceptions import *
from marshmallow import ValidationError
from routes.initializer import errors
"""
Managing the error in different app and routes
Flask have capability of managing blueprint and the routes
All exceptions are loaded here
"""


@errors.app_errorhandler(ModelNotFoundException)
def handle_model_constraint(error):
    return error.to_dict()


@errors.app_errorhandler(code=404)
def handle_not_found(error):
    http_404 = NotFoundException('sorry, url requested not found', 404, error)
    return http_404.to_dict()


@errors.app_errorhandler(code=400)
def handle_bad_request(error):
    http_400 = BadRequestException(error, 400)
    return http_400.to_dict()


@errors.app_errorhandler(ValidationError)
def handle_validation_errors(error):
    validation = ValidationException(error.messages, 400)
    return validation.to_dict()


@errors.app_errorhandler(Exception)
def handle_bad_request(error):
    http_500 = ServerInternalError({'server': 'internal server error encountered'}, 500)
    return http_500.to_dict()

