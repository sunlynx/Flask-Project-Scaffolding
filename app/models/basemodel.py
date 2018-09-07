from database.initializer import db
from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID


class BaseModel(db.Model):
    """
    Base model contains all the basic functionality needed for other model to have DRY and SOLID principles
    """
    __abstract__ = True
    id = Column(UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()", )
