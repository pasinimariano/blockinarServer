create_category_schema = {
    "category_name": {"minlength": 2,"maxlength": 60, "required": True, "regex": r'[A-z]+'},
    "price": {"required": False, "regex": r'[0-9]+'},
}
