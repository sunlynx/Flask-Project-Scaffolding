from routes.initializer import router
from app.controllers.locations.governatecontroller import GovernateController

"""
Prefix the API using the group
"""
router.add_resource(GovernateController, '/admin/governate')
