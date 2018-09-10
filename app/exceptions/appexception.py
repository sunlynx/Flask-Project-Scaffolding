from flask import jsonify
"""
AppException class extends flask exception base class and overrides the property
This contain reusable code, they are not following any structural, behavioural, creation design pattern
Write code that is going to use in further classes. Also write elaborated messages
"""


class AppException(Exception):
    status_code = 401

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.error_message = message
        self.status_code = status_code if status_code is not None else self.status_code
        self.payload = payload

    def to_dict(self):
        """
        Return the response as a structured one
        :return:
        """
        response_construct = jsonify({
            'status': 'failure',
            'data': [],
            'error': {
                'err_code': self.status_code,
                'err_message': self.error_message,
            },
        })

        response_construct.status_code = self.status_code
        return response_construct
