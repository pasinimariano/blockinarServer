class CategoriesService:
    def __init__(self, db, categories_model, category_name=None, price=None):
        self.db = db
        self.CategoryModel = categories_model
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
