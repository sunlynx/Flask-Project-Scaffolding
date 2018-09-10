from app.models.locations import Areas, AreaSchema
from flask import request
from app.exceptions.systemexceptions import ModelNotFoundException
from app.controllers.basecontroller import BaseController
from marshmallow import ValidationError
from lib.messages import Messages
from run import db


class AreasController(BaseController):
    """
    Governate is a resource, super admin can perform CRUD operations on it
    Flask restful assign GET request to get method, similarly to other HTTP Request
    """

    def __init__(self):
        """
        call base controller constructor to initialize the class
        use middleware here
        """
        super(AreasController, self).__init__()
        self.schemas = AreaSchema(strict=True, many=True)
        self.schema = AreaSchema(strict=True, many=False)

    def get(self):
        """
        Return list of records of governates with areas
        You have to override the properties
        data_set, status_code and error_message
        call the serializer
        :return:
        """
        self.data_set = self.schemas.dump(Areas.query.all()).data
        return self.response()

    def post(self):
        """
        Validate all the request parameters
        :return:
        """
        area_load, errors = self.schema.load(request.get_json(), partial=('id', ))
        if errors:
            raise ValidationError(errors)
        area = Areas(**area_load)
        db.session.add(area)
        db.session.commit()
        self.data_set = self.schema.dump(area).data
        return self.response()

    def put(self):
        """
        validate the request, and return object
        :return:
        """
        area_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        area = Areas.query.get(area_load['id'])
        if area is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)

        area.governates_id = area_load['governates_id']
        area.code = area_load['code']
        area.name = area_load['name']
        db.session.commit()

        self.data_set = self.schema.dump(area).data
        return self.response()

    def delete(self):
        """
        validate the request, and return object
        :return:
        """
        area_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        area = Areas.query.get(area_load['id'])
        if area is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)
        db.session.delete(area)
        db.session.commit()

        self.data_set = Messages.SUCCESSFULLY_DELETED
        return self.response()
