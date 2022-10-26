def set_admin_schema(marshmallow, admin_model):
    class AdminSchema(marshmallow.Schema):
        class Meta:
            fields = ("id",
                      "first_name",
                      "last_name",
                      "email")
            model = admin_model

    return AdminSchema


def set_bookings_schema(marshmallow, bookings_model):
    class BookingsSchema(marshmallow.Schema):
        class Meta:
            fields = ("id",
                      "first_name",
                      "last_name",
                      "check_in_date",
                      "check_out_date",
                      "number_of_guests"
                      "price_per_night",
                      "status",
                      "room_id")

            model = bookings_model

    return BookingsSchema


def set_rooms_schema(marshmallow, rooms_model):
    class RoomsSchema(marshmallow.Schema):
        class Meta:
            fields = ("id",
                      "occupancy",
                      "max_occupancy",
                      "category_id")
            model = rooms_model

    return RoomsSchema


def set_categories_schema(marshmallow, categories_model, many):
    class CategoriesSchema(marshmallow.Schema):
        class Meta:
            fields = ("id",
                      "category_name",
                      "price")
            model = categories_model

    categories_schema = CategoriesSchema(many=many)

    return categories_schema


def set_status_schema(marshmallow, status_model, many):
    class StatusSchema(marshmallow.Schema):
        class Meta:
            fields = ("id",
                      "booking_status")
            model = status_model

    status_schema = StatusSchema(many=many)

    return status_schema
