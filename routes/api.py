from routes.initializer import router
from app.controllers.locations.governatecontroller import GovernateController
from app.controllers.locations.areascontroller import AreasController


"""
Prefix the API using the group
"""
router.add_resource(GovernateController, '/admin/governate')
router.add_resource(AreasController, '/admin/area')
