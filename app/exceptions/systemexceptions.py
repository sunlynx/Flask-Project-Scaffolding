from app.exceptions.appexception import AppException

"""
All Exception are going to be handles in the exception directory of app
There are three files managing: AppException, Handler, and SystemExceptions
This directory has a separate blueprint and handles rest of the things here only  
"""


class SystemExceptions(AppException):
    def __init__(self, message, *args, **kwargs):
        super(SystemExceptions, self).__init__(message, status_code=None, payload=None)


class UniqueConstraintException(AppException):
    def __init__(self, message, *args, **kwargs):
        super(UniqueConstraintException, self).__init__(message, status_code=None, payload=None)

