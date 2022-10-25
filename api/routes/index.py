from api.routes.admins import admins_routes


def get_routes(api, admin_model, db):
    admins_routes(api, admin_model, db)
