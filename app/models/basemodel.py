from database.initializer import db
import datetime
from sqlalchemy import Column, DateTime, text
from sqlalchemy.dialects.postgresql import UUID


class BaseModel(db.Model):
    """
    Base model contains all the basic functionality needed for other model to have DRY and SOLID principles
    """
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("uuid_generate_v4()"), )
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.now)
