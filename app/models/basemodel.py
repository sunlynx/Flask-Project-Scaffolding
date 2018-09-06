from database.initializer import db


class BaseModel(db.Model):
    """
    Base model contains all the basic functionality needed for other model to have DRY and SOLID principles
    """
    def __init__(self):
        pass

