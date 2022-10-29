regex_letters = r'[A-z]+'
regex_password = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,128}$'
regex_email = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

create_admin_schema = {
    "first_name": {"minlength": 2, "maxlength": 60, "required": True, 'regex': regex_letters},
    "last_name": {"minlength": 2, "maxlength": 60, "required": True, 'regex': regex_letters},
    "email": {"maxlength": 128, "required": True, "regex": regex_email},
    "password": {"minlength": 8, "maxlength": 128, "required": True, "regex": regex_password},
    "role": {"required": True}
}

login_admin_schema = {
    "email": {"maxlength": 128, "required": True, "regex": regex_email},
    "password": {"minlength": 8, "maxlength": 128, "required": True, "regex": regex_password},
}