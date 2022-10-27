from api.db.models import Rooms, db


class RoomsService:
    def __init__(self, room_id=None, occupancy=None,
                 max_occupancy=None, category_id=None):
        self.room_id = room_id
        self.occupancy = occupancy
        self.max_occupancy = max_occupancy
        self.category_id = category_id

    def get_all_rooms(self):
        try:
            rooms = Rooms.query.all()

            return {"ok": True, "rooms": rooms}
        except Exception as error:
            print(" * Error when trying to get Rooms")
            return {"ok": False, "error": error}

    def create_new_room(self):
        try:
            room = Rooms(
                occupancy=self.occupancy,
                max_occupancy=self.max_occupancy,
                category_id=self.category_id
            )

            db.session.add(room)
            db.session.commit()

            print(" * Room created successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Room")
            return {"ok": False, "error": error}

    def update_room(self):
        try:
            room = Rooms.query.filter_by(id=self.room_id).first()
            room.occupancy = self.occupancy
            room.max_occupancy = self.max_occupancy
            room.category_id = self.category_id

            db.session.commit()

            print(" * Room updated successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Room")
            return {"ok": False, "error": error}

    def delete_room(self):
        try:
            room = Rooms.query.filter_by(id=self.room_id).first()

            db.session.delete(room)
            db.session.commit()

            print(" * Room deleted successfully")
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Room")
            return {"ok": False, "error": error}


