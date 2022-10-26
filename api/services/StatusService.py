class StatusService:
    def __init__(self, db, status_model, status_id=None, booking_status=None):
        self.db = db
        self.StatusModel = status_model
        self.status_id = status_id
        self.booking_status = booking_status

    def get_all_status(self):
        try:
            status = self.StatusModel.query.all()

            return {"ok": True, "status": status}
        except Exception as error:
            print(" * Error when trying to get Categories")
            return {"ok": False, "error": error}

    def create_new_status(self):
        try:
            status = self.StatusModel(
                booking_status=self.booking_status,
            )

            self.db.session.add(status)
            self.db.session.commit()

            print(" * Status {} created successfully".format(self.booking_status))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Status")
            return {"ok": False, "error": error}

    def update_status(self):
        try:
            status = self.StatusModel.query.filter_by(id=self.status_id).first()
            status.booking_status = self.booking_status

            self.db.session.commit()

            print(" * Status {} updated successfully".format(self.status_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Status")
            return {"ok": False, "error": error}

    def delete_status(self):
        try:
            status = self.StatusModel.query.filter_by(id=self.status_id).first()

            self.db.session.delete(status)
            self.db.session.commit()

            print(" * Category {} deleted successfully".format(self.status_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Status")
            return {"ok": False, "error": error}
