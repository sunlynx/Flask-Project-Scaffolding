from app.exceptions.appexception import AppException

"""
All Exception are going to be handles in the exception directory of app
There are three files managing: AppException, Handler, and SystemExceptions
This directory has a separate blueprint and handles rest of the things here only  
"""


class SystemExceptions(AppException):
    def __init__(self, message, *args, **kwargs):
        super(SystemExceptions, self).__init__(message, status_code=None, payload=None)


class ModelNotFoundException(AppException):
    def __init__(self, message, *args, **kwargs):
        super(ModelNotFoundException, self).__init__(message, status_code=None, payload=None)


class NotFoundException(AppException):
    def __init__(self, message, *args, **kwargs):
        super(NotFoundException, self).__init__(message=message, status_code=404, payload=None)


class BadRequestException(AppException):
    def __init__(self, message, *args, **kwargs):
        super(BadRequestException, self).__init__(message=message, status_code=404, payload=None)


class ValidationException(AppException):
    def __init__(self, message, *args, **kwargs):
        super(ValidationException, self).__init__(message=message, status_code=404, payload=None)
        self.error_message = {}
        for key, value in message.items():
            self.error_message[key] = " ,".join(value)


class ServerInternalError(AppException):
    def __init__(self, message, *args, **kwargs):
        super(ServerInternalError, self).__init__(message=message, status_code=500, payload=None)
