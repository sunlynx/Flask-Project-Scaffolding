from flask import jsonify
from flask_restful import Resource


class BaseController(Resource):
    """
    Setup your base controller to provide basic functionality and helper alongside
    Constructor is access when derived called super() method
    Also this function defines how to validate the request from serializer and response
    """
    data_set = []
    status_code = 200
    error_message = None

    def __init__(self):
        pass

    def response(self):
        """
        Return the response as a structured one
        :return:
        """
        response_construct = jsonify({
            'status': 'success',
            'data': self.data_set,
            'error': {
               'err_code': self.status_code,
               'err_message': self.error_message
            },
        })
        response_construct.status_code = self.status_code
        return response_construct
