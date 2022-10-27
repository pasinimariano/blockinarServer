from marshmallow import Schema, fields

AdminSchema = Schema.from_dict(
    {
        "id": fields.Int(),
        "first_name": fields.Str(),
        "last_name": fields.Str(),
        "email": fields.Email(),
        "role": fields.Int()
    }
)

BookingSchema = Schema.from_dict(
    {
        "id": fields.Int(),
        "first_name": fields.Str(),
        "last_name": fields.Str(),
        "check_in_date": fields.DateTime(),
        "check_out_date": fields.DateTime(),
        "number_of_guests": fields.Int(),
        "price_per_night": fields.Int()
    }
)

RoomsSchema = Schema.from_dict(
    {
        "id": fields.Int(),
        "occupancy": fields.Int(),
        "max_occupancy": fields.Int()
    }
)

CategoriesSchema = Schema.from_dict(
    {
        "id": fields.Int(),
        "category_name": fields.Str(),
        "price": fields.Int()
    }
)

StatusSchema = Schema.from_dict(
    {
        "id": fields.Int(),
        "booking_status": fields.Str()
    }
)
