class AdminService:
    def __init__(self, api, admin_model, db, password, email, first_name=None, last_name=None, role=None, _id=None):
        self.api = api
        self.AdminModel = admin_model
        self.db = db
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self._id = _id

    def create_new_admin(self):
        try:
            admin = self.AdminModel(
                first_name=self.first_name,
                last_name=self.last_name,
                email=self.email,
                password=self.password,
                role=self.role
                                    )

            self.db.session.add(admin)
            self.db.session.commit()

            print(" * Admin {} {} created successfully".format(self.first_name, self.last_name))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Admin")
            return {"ok": False, "error": error}
