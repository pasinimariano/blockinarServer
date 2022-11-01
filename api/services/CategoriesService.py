from api.db.models import Categories, db


class CategoriesService:
    def __init__(self, category_id=None, category_name=None, price=None):
        self.category_id = category_id
        self.category_name = category_name
        self.price = price

    def get_all_categories(self):
        try:
            categories = Categories.query.all()

            db.session.commit()

            return {"ok": True, "categories": categories}
        except Exception as error:
            print(" * Error when trying to get Categories")
            return {"ok": False, "error": error}

    def create_new_category(self):
        try:
            category = Categories(
                category_name=self.category_name,
                price=self.price
            )

            db.session.add(category)
            db.session.commit()

            print(" * Category {} created successfully".format(self.category_name))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to create Category")
            return {"ok": False, "error": error}

    def update_category(self):
        try:
            category = Categories.query.filter_by(id=self.category_id).first()
            category.category_name = self.category_name
            category.price = self.price

            db.session.commit()

            print(" * Category {} updated successfully".format(self.category_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to update Category")
            return {"ok": False, "error": error}

    def delete_category(self):
        try:
            category = Categories.query.filter_by(id=self.category_id).first()

            db.session.delete(category)
            db.session.commit()

            print(" * Category {} deleted successfully".format(self.category_id))
            return {"ok": True, "msg": "Success"}

        except Exception as error:
            print(" * Error when trying to delete Category")
            return {"ok": False, "error": error}
