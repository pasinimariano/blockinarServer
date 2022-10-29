from api.routes.admins import admins_routes
from api.routes.categories import categories_routes
from api.routes.status import status_routes
from api.routes.rooms import rooms_routes
from api.routes.bookings import bookings_routes


def get_routes(api):
    admins_routes(api)
    categories_routes(api)
    status_routes(api)
    rooms_routes(api)
    bookings_routes(api)
