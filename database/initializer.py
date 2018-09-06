from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


db = SQLAlchemy()
migrate = Migrate(db=db)
from app.models.locations import Governates, Areas, Villages

"""
Below are the commands used to run migrations and other operations
"""
# flask db init
# flask db migrate
# flask db upgrade
# flask db --help
