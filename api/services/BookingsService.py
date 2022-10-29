from api.db.models import Bookings, db


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
            bookings = Bookings.query.all()

            return {"ok": True, "bookings": bookings}
        except Exception as error:
            print(" * Error when trying to get Bookings")
            return {"ok": False, "error": error}

    def create_new_booking(self):
        try:
            date_in = "{}T{}".format(self.check_in_date[0:10], self.check_in_date[10:])
            date_out = "{}T{}".format(self.check_out_date[0:10], self.check_out_date[10:])
            guests = self.number_of_guests if self.number_of_guests.isnumeric() else None
            price = self.price_per_night if self.price_per_night.isnumeric() else None
            status = self.status_id if self.status_id.isnumeric() else 1
            room = self.room_id if self.room_id.isnumeric() else None

            booking = Bookings(
                first_name=self.first_name,
                last_name=self.last_name,
                check_in_date=date_in,
                check_out_date=date_out,
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
        date_in = "{}T{}".format(self.check_in_date[0:10], self.check_in_date[10:])
        date_out = "{}T{}".format(self.check_out_date[0:10], self.check_out_date[10:])
        guests = self.number_of_guests if self.number_of_guests.isnumeric() else None
        price = self.price_per_night if self.price_per_night.isnumeric() else None
        status = self.status_id if self.status_id.isnumeric() else 1
        room = self.room_id if self.room_id.isnumeric() else None

        try:
            booking = Bookings.query.filter_by(id=self.booking_id).first()
            booking.first_name = self.first_name
            booking.last_name = self.last_name
            booking.check_in_date = date_in
            booking.check_out_date = date_out
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

