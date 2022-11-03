from api.db.models import Bookings, Rooms, Status, db
from api.db.marshmallows import StatusSchema
from sqlalchemy import and_, func
from datetime import datetime


class BookingsService:
    def __init__(self, booking_id=None, first_name=None, last_name=None, check_in_date=None, check_out_date=None,
                 number_of_guests=None, price_per_night=None, status_id=None, room_id=None):
        self.booking_id = booking_id
        self.first_name = first_name
        self.last_name = last_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.number_of_guests = number_of_guests
        self.price_per_night = price_per_night
        self.status_id = status_id
        self.room_id = room_id

    def get_all_bookings(self):
        try:
            if self.check_in_date is not None:
                day_bookings = Bookings.query\
                    .filter(func.date(Bookings.check_in_date) == func.date(self.check_in_date)).all()
                checked = Bookings.query.filter_by(status_id=3)\
                    .filter(func.date(Bookings.check_in_date) < self.check_in_date).all()
                bookings = list(set(day_bookings + checked))

            elif self.booking_id is not None:
                bookings = Bookings.query.filter_by(id=self.booking_id).all()
            elif self.last_name is not None:
                bookings = Bookings.query.filter_by(last_name=self.last_name).all()
            else:
                bookings = Bookings.query.all()

            db.session.commit()

            return {"ok": True, "bookings": bookings}
        except Exception as error:
            print(" * Error when trying to get Bookings")
            return {"ok": False, "error": error}

    def create_new_booking(self):
        try:
            guests = self.number_of_guests if type(self.number_of_guests) == int else None
            price = self.price_per_night if type(self.price_per_night) == int else None
            status = self.status_id if type(self.status_id) == int else 1
            room = self.room_id if type(self.room_id) == int else None

            booking = Bookings(
                first_name=self.first_name,
                last_name=self.last_name,
                check_in_date=self.check_in_date,
                check_out_date=self.check_out_date,
                number_of_guests=guests,
                price_per_night=price,
                status_id=status,
                room_id=room
            )

            db.session.add(booking)
            db.session.commit()

            print(" * Booking created successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Booking")
            return {"ok": False, "error": error}

    def update_booking(self):
        guests = self.number_of_guests if type(self.number_of_guests) == int else None
        price = self.price_per_night if type(self.price_per_night) == int else None
        status = self.status_id if type(self.status_id) == int else 1
        room = self.room_id if type(self.room_id) == int else None
        get_status = {}

        if status is not None:
            status_schema = StatusSchema()
            filter_status = Status.query.filter_by(id=status).first()
            get_status = status_schema.dump(filter_status)

        if get_status["booking_status"] == "Checked In" and room is not None:
            room_occupancy = Rooms.query.filter_by(id=self.room_id).first()
            room_occupancy.occupancy = 1

        if get_status["booking_status"] == "Checked Out":
            room_occupancy = Rooms.query.filter_by(id=self.room_id).first()
            room_occupancy.occupancy = 0

        try:
            booking = Bookings.query.filter_by(id=self.booking_id).first()
            booking.first_name = self.first_name
            booking.last_name = self.last_name
            booking.check_in_date = self.check_in_date
            booking.check_out_date = self.check_out_date
            booking.number_of_guests = guests
            booking.price_per_night = price
            booking.status_id = status
            booking.room_id = room

            db.session.commit()

            print(" * Booking updated successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Booking")
            return {"ok": False, "error": error}

    def delete_booking(self):
        try:
            booking = Bookings.query.filter_by(id=self.booking_id).first()

            db.session.delete(booking)
            db.session.commit()

            print(" * Booking deleted successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Booking")
            return {"ok": False, "error": error}


