from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from lib.messages import Messages
from werkzeug.security import safe_str_cmp
from sqlalchemy.dialects.postgresql import UUID
from marshmallow import Schema, fields, validates, ValidationError


class Governates(BaseModel):
    """
    Locations having governate, and each governate has many areas
    Relationship: governate has many areas
    Use if necessary:
    default_fields = ['name', 'code']
    hidden_fields = ['code']
    readonly_fields = ['code']
    """
    __tablename__ = 'governates'

    name = Column(String(191), nullable=False,)
    code = Column(String(30), nullable=False, unique=True,)
    areas = relationship("Areas", backref="governates")     # Bi-Directional Relationship

    def __init__(self, name, code, *argss, **kwargs):
        self.name = name
        self.code = code

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class Areas(BaseModel):
    """
    Locations having governate, and each governate has many areas
    Relationship: areas belongs to many governates
    """
    __tablename__ = 'areas'

    name = Column(String(191), nullable=False, )
    code = Column(String(30), nullable=False, unique=True,)
    governates_id = Column(UUID(as_uuid=True), ForeignKey('governates.id'))
    villages = relationship("Villages", backref="areas")

    def __init__(self, name, code, governates_id,  *argss, **kwargs):
        self.name = name
        self.code = code
        self.governates_id = governates_id

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


class Villages(BaseModel):
    """
    Locations having governate, and each governate has many areas and each are has many villages
    Relationship: areas has many villages
    """
    __tablename__ = 'villages'

    name = Column(String(191), nullable=False, )
    code = Column(String(30), nullable=False, unique=True, )
    areas_id = Column(UUID(as_uuid=True), ForeignKey('areas.id'))

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)


"""
All schema goes here
"""


class VillageSchema(Schema):
    class Meta:
        ordered = True

    id = fields.UUID(required=True)
    name = fields.String(required=True)
    code = fields.String(required=True)
    areas_id = fields.UUID(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    @validates('code')
    def validate_unique_code(self, value):
        village = Villages.query.filter_by(code=value).first()
        if (village is not None) and (not safe_str_cmp(village.code, value)):
            raise ValidationError(Messages.UNIQUE_EXCEPTION.format(value))

    @validates('areas_id')
    def validates_villages_existence(self, value):
        if Areas.query.get(value) is None:
            raise ValidationError(Messages.NOT_EXISTS.format(value))


class AreaSchema(Schema):
    class Meta:
        ordered = True

    id = fields.UUID(required=True)
    name = fields.String(required=True)
    code = fields.String(required=True)
    governates_id = fields.UUID(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    villages = fields.Nested(VillageSchema, many=True)

    @validates('code')
    def validate_unique_code(self, value):
        area = Areas.query.filter_by(code=value).first()
        if (area is not None) and (not safe_str_cmp(area.code, value)):
            raise ValidationError(Messages.UNIQUE_EXCEPTION.format(value))

    @validates('governates_id')
    def validates_governates_existence(self, value):
        if Governates.query.get(value) is None:
            raise ValidationError(Messages.NOT_EXISTS.format(value))


class GovernateSchema(Schema):
    class Meta:
        ordered = True

    id = fields.UUID(required=True)
    name = fields.String(required=True)
    code = fields.String(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    areas = fields.Nested(AreaSchema, many=True)

    @validates('code')
    def validate_unique_code(self, value):
        governate = Governates.query.filter_by(code=value).first()
        if (governate is not None) and (not safe_str_cmp(governate.code, value)):
            raise ValidationError(Messages.UNIQUE_EXCEPTION.format(value))
    #
    # formatted_name = fields.Method('format_name', dump_only=True)
    # fields = ('id', 'name', 'code', 'created_at')
    # def format_name(self, author):
    #     return '{}, {}'.format(author.last, author.first)

