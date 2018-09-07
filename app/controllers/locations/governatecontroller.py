from flask_restful import Resource
from app.models.locations import Governates
from app.controllers.basecontroller import BaseController


class GovernateController(BaseController, Resource):
    """
    Governate is a resource, super admin can perform CRUD operations on it
    Flask restful assign GET request to get method, similarly to other HTTP Request
    """
    def __init__(self):
        """
        call base controller constructor to initialize the class
        use middleware here
        """
        super(GovernateController, self).__init__()
        pass

    def get(self):
        """
        Return list of records of governates with areas
        You have to override the properties
        data_set, status_code and error_message
        :return:
        """
        self.data_set = Governates.query.all()
        return self.response()

    def post(self):
       pass
