class CategoriesService:
    def __init__(self, db, categories_model, category_id=None, category_name=None, price=None):
        self.db = db
        self.CategoryModel = categories_model
        self.category_id = category_id
        self.category_name = category_name
        self.price = price

    def get_all_categories(self):
        try:
            categories = self.CategoryModel.query.all()

            return {"ok": True, "categories": categories}
        except Exception as error:
            print(" * Error when trying to get Categories")
            return {"ok": False, "error": error}

    def create_new_category(self):
        try:
            category = self.CategoryModel(
                category_name=self.category_name,
                price=self.price
            )

            self.db.session.add(category)
            self.db.session.commit()

            print(" * Category {} created successfully".format(self.category_name))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Category")
            return {"ok": False, "error": error}

    def update_category(self):
        try:
            category = self.CategoryModel.query.filter_by(id=self.category_id).first()
            category.category_name = self.category_name
            category.price = self.price

            self.db.session.commit()

            print(" * Category {} updated successfully".format(self.category_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Category")
            return {"ok": False, "error": error}

    def delete_category(self):
        try:
            category = self.CategoryModel.query.filter_by(id=self.category_id).first()

            self.db.session.delete(category)
            self.db.session.commit()

            print(" * Category {} deleted successfully".format(self.category_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Category")
            return {"ok": False, "error": error}
