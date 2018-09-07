from flask_restful import Resource, reqparse
from app.models.locations import Governates
from app.exceptions.systemexceptions import UniqueConstraintException
from app.controllers.basecontroller import BaseController
from app.serializers.governateserializer import GovernateSerializer
from lib.messages import Messages
from run import db


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
        call the serializer
        :return:
        """
        self.data_set = Governates.query.all()
        return self.response()

    def post(self):
        """
        Validate all the request parameters
        :return:
        """
        arguments = GovernateSerializer(reqparse.RequestParser(bundle_errors=True)).post()
        if Governates.query.filter_by(code=arguments['code']).first() is not None:
            raise UniqueConstraintException(Messages.UNIQUE_EXCEPTION.format('code'))
        governate = Governates(**arguments)
        db.session.add(governate)
        db.session.commit()
        self.data_set = [Messages.GOVERNATE_INSERTED]
        return self.response()
