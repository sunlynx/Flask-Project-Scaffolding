from app.models.locations import Governates, GovernateSchema
from flask import request
from app.exceptions.systemexceptions import ModelNotFoundException
from app.controllers.basecontroller import BaseController
from marshmallow import ValidationError
from lib.messages import Messages
from run import db


class GovernateController(BaseController):
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
        self.schemas = GovernateSchema(strict=True, many=True)
        self.schema = GovernateSchema(strict=True, many=False)

    def get(self):
        """
        Return list of records of governates with areas
        You have to override the properties
        data_set, status_code and error_message
        call the serializer
        :return:
        """
        self.data_set = self.schemas.dump(Governates.query.all()).data
        return self.response()

    def post(self):
        """
        Validate all the request parameters
        :return:
        """
        governate_load, errors = self.schema.load(request.get_json())
        if errors:
            raise ValidationError(errors)
        governate = Governates(**governate_load)
        db.session.add(governate)
        db.session.commit()
        self.data_set = self.schema.dump(governate).data
        return self.response()

    def put(self):
        """
        validate the request, and return object
        :return:
        """
        governate_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        governate = Governates.query.get(governate_load['id'])
        if governate is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)
        governate.code = governate_load['code']
        governate.name = governate_load['name']
        db.session.commit()

        self.data_set = self.schema.dump(governate).data
        return self.response()

    def delete(self):
        """
        validate the request, and return object
        :return:
        """
        governate_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        governate = Governates.query.get(governate_load['id'])
        if governate is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)
        db.session.delete(governate)
        db.session.commit()

        self.data_set = Messages.SUCCESSFULLY_DELETED
        return self.response()
