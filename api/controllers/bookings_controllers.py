from flask import request
from functools import wraps

from api.utils.send_errors import send_invalid_error, send_internal_error
from api.utils.token_generator import token_decode, token_generator
from api.services.BookingsService import BookingsService
from api.db.marshmallows import BookingSchema

marshmallow = BookingSchema(many=True)


def get_all_rooms_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    service = BookingsService()
                    token = request.headers.get('token')
                    email = token_decode(token)

                    all_bookings = service.get_all_bookings()

                    if all_bookings["ok"] is False:
                        return send_invalid_error(all_bookings["error"])

                    serialized_bookings = marshmallow.dump(all_bookings["bookings"])
                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"bookings": serialized_bookings, "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def create_booking_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    req = request.json
                    first_name, last_name = req["first_name"], req["last_name"]
                    check_in_date, check_out_date = req["check_in_date"], req["check_out_date"]
                    number_of_guests, price_per_night = req["number_of_guests"], req["price_per_night"]
                    status_id, room_id = req["status_id"], req["room_id"]

                    service = BookingsService(first_name=first_name, last_name=last_name, check_in_date=check_in_date,
                                              check_out_date=check_out_date, number_of_guests=number_of_guests,
                                              price_per_night=price_per_night, status_id=status_id, room_id=room_id)

                    token = request.headers.get('token')
                    email = token_decode(token)

                    new_booking = service.create_new_booking()

                    if new_booking["ok"] is False:
                        return send_invalid_error(new_booking["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def update_room_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    booking_id = request.args.get("id")
                    req = request.json
                    first_name, last_name = req["first_name"], req["last_name"]
                    check_in_date, check_out_date = req["check_in_date"], req["check_out_date"]
                    number_of_guests, price_per_night = req["number_of_guests"], req["price_per_night"]
                    status_id, room_id = req["status_id"], req["room_id"]

                    service = BookingsService(booking_id, first_name, last_name, check_in_date, check_out_date,
                                              number_of_guests, price_per_night, status_id, room_id)

                    token = request.headers.get('token')
                    email = token_decode(token)

                    update_booking = service.update_booking()

                    if update_booking["ok"] is False:
                        return send_invalid_error(update_booking["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator


def delete_room_controller(api):
    def decorator(func):
        @wraps(func)
        def wrapper():
            with api.app_context():
                try:
                    booking_id = request.args.get("id")
                    token = request.headers.get('token')
                    email = token_decode(token)

                    service = BookingsService(booking_id)

                    delete_booking = service.delete_booking()

                    if delete_booking["ok"] is False:
                        return send_invalid_error(delete_booking["error"])

                    new_token = token_generator(email)

                    if new_token["ok"] is False:
                        return send_invalid_error(new_token["error"])

                    return func({"msg": "Success", "token": new_token["token"]})

                except Exception as error:
                    return send_internal_error(error)

        return wrapper
    return decorator
