from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Integer(), nullable=False)


class Bookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    check_in_date = db.Column(db.DateTime(), nullable=False)
    check_out_date = db.Column(db.DateTime(), nullable=False)
    number_of_guests = db.Column(db.Integer())
    price_per_night = db.Column(db.Integer())
    status_id = db.Column(db.Integer, db.ForeignKey("status.id"))
    room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))


class Rooms(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    occupancy = db.Column(db.Integer)
    max_occupancy = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    bookings = db.relationship("Bookings", backref="room")


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(60), unique=True, nullable=False)
    price = db.Column(db.Integer)
    rooms = db.relationship("Rooms", backref="category")


class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_status = db.Column(db.String(60), unique=True, nullable=False)
    bookings = db.relationship("Bookings", backref="booking_status")


