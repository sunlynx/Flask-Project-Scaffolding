from flask import request, jsonify, Response


class BaseController:
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
        response_construct = {
            'status': 'success',
            'data': self.data_set,
            'error_message': self.error_message,
        }
        return Response(response_construct, status=self.status_code,  mimetype='application/json')
