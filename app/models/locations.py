from app.models.basemodel import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


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

    def __init__(self, name, code):
        self.name = name
        self.code = code


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


class Villages(BaseModel):
    """
    Locations having governate, and each governate has many areas and each are has many villages
    Relationship: areas has many villages
    """
    __tablename__ = 'villages'

    name = Column(String(191), nullable=False, )
    code = Column(String(30), nullable=False, unique=True, )
    areas_id = Column(UUID(as_uuid=True), ForeignKey('areas.id'))
