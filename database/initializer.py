from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate(db=db)

"""
Below are the commands used to run migrations and other operations
"""
# flask db init
# flask db migrate
# flask db upgrade
# flask db --help
