def admin(db):
    class Admin(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(60), nullable=False)
        last_name = db.Column(db.String(60), nullable=False)
        email = db.Column(db.String(128), nullable=False, unique=True)
        password = db.Column(db.String(128), nullable=False)
        role = db.Column(db.Integer(), nullable=False)

    return Admin


def bookings(db):
    class Bookings(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        first_name = db.Column(db.String(60), nullable=False)
        last_name = db.Column(db.String(60), nullable=False)
        check_in_date = db.Column(db.DateTime(), nullable=False)
        check_out_date = db.Column(db.DateTime(), nullable=False)
        number_of_guests = db.Column(db.Integer())
        price_per_night = db.Column(db.Integer())
        status = db.Column(db.Integer, db.ForeignKey("status.id"), nullable=False)
        room_id = db.Column(db.Integer, db.ForeignKey("rooms.id"))

        def __repr__(self):
            return "<Bookings %s>" % self.id

    return Bookings


def rooms(db):
    class Rooms(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        occupancy = db.Column(db.Integer)
        max_occupancy = db.Column(db.Integer)
        category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
        bookings = db.relationship("Bookings", backref="booking", lazy=True)

        def __repr__(self):
            return "<Rooms %s>" % self.id

    return Rooms


def categories(db):
    class Categories(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        category_name = db.Column(db.String(60), unique=True, nullable=False)
        price = db.Column(db.Integer)
        rooms = db.relationship("Rooms", backref="room", lazy=True)

        def __repr__(self):
            return "<Categories %s>" % self.id

    return Categories


def status(db):
    class Status(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        booking_status = db.Column(db.String(60), unique=True, nullable=False)
        bookings = db.relationship("Bookings", backref="booking_status", lazy=True)

        def __repr__(self):
            return "<Status %s>" % self.id

    return Status
