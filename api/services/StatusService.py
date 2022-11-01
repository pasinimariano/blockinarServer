from api.db.models import Status, db


class StatusService:
    def __init__(self, status_id=None, booking_status=None):
        self.status_id = status_id
        self.booking_status = booking_status

    def get_all_status(self):
        try:
            status = Status.query.all()

            db.session.commit()

            return {"ok": True, "status": status}
        except Exception as error:
            print(" * Error when trying to get Categories")
            return {"ok": False, "error": error}

    def create_new_status(self):
        try:
            status = Status(
                booking_status=self.booking_status,
            )

            db.session.add(status)
            db.session.commit()

            print(" * Status {} created successfully".format(self.booking_status))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Status")
            return {"ok": False, "error": error}

    def update_status(self):
        try:
            status = Status.query.filter_by(id=self.status_id).all()
            status.booking_status = self.booking_status

            db.session.commit()

            print(" * Status {} updated successfully".format(self.status_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Status")
            return {"ok": False, "error": error}

    def delete_status(self):
        try:
            status = Status.query.filter_by(id=self.status_id).all()

            db.session.delete(status)
            db.session.commit()

            print(" * Category {} deleted successfully".format(self.status_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Status")
            return {"ok": False, "error": error}
