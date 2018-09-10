from app.models.locations import Villages, VillageSchema
from flask import request
from app.exceptions.systemexceptions import ModelNotFoundException
from app.controllers.basecontroller import BaseController
from marshmallow import ValidationError
from lib.messages import Messages
from run import db


class VillageController(BaseController):
    """
    Governate is a resource, super admin can perform CRUD operations on it
    Flask restful assign GET request to get method, similarly to other HTTP Request
    """

    def __init__(self):
        """
        call base controller constructor to initialize the class
        use middleware here
        """
        super(VillageController, self).__init__()
        self.schemas = VillageSchema(strict=True, many=True)
        self.schema = VillageSchema(strict=True, many=False)

    def get(self):
        """
        Return list of records of governates with areas
        You have to override the properties
        data_set, status_code and error_message
        call the serializer
        :return:
        """
        self.data_set = self.schemas.dump(Villages.query.all()).data
        return self.response()

    def post(self):
        """
        Validate all the request parameters
        :return:
        """
        village_load, errors = self.schema.load(request.get_json(), partial=('id', ))
        if errors:
            raise ValidationError(errors)
        village = Villages(**village_load)
        db.session.add(village)
        db.session.commit()
        self.data_set = self.schema.dump(village).data
        return self.response()

    def put(self):
        """
        validate the request, and return object
        :return:
        """
        village_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        village = Villages.query.get(village_load['id'])
        if village is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)

        village.areas_id = village_load['areas_id']
        village.code = village_load['code']
        village.name = village_load['name']
        db.session.commit()

        self.data_set = self.schema.dump(village).data
        return self.response()

    def delete(self):
        """
        validate the request, and return object
        :return:
        """
        village_load = self.schema.load(request.get_json(), partial=('code', 'name', )).data
        village = Villages.query.get(village_load['id'])
        if village is None:
            raise ModelNotFoundException(Messages.NO_RECORD_FOUND)
        db.session.delete(village)
        db.session.commit()

        self.data_set = Messages.SUCCESSFULLY_DELETED
        return self.response()
