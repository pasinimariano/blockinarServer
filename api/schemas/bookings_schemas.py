regex_number = r'^(\s*|\d+)$'
regex_letters = r'[A-z]+'
regex_dates = "^(?:\\d{4})-(?:\\d{2})-(?:\\d{2})(?:\\d{2})" \
              ":(?:\\d{2}):(?:\\d{2}(?:\\.\\d*)?)(?:(?:-(?:\\d{2}):(?:\\d{2})|Z)?)$"

create_booking_schema = {
    "first_name": {"minlength": 2, "maxlength": 60, "required": True, "regex": regex_letters},
    "last_name": {"minlength": 2, "maxlength": 60, "required": True, "regex": regex_letters},
    "check_in_date": {"required": True, "regex": regex_dates},
    "check_out_date": {"required": True, "regex": regex_dates},
    "number_of_guests": {"required": False, "regex": regex_number},
    "price_per_night": {"required": False, "regex": regex_number},
    "status_id": {"required": False, "regex": regex_number},
    "room_id": {"required": False, "regex": regex_number}
}
