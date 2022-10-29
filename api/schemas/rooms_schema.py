regex_number = r'[0-9]+'

create_room_schema = {
    "occupancy": {"required": True, 'regex': regex_number},
    "max_occupancy": {"required": True, 'regex': regex_number},
    "category_id": {"required": True, 'regex': regex_number},
}