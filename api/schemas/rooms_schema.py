create_room_schema = {
    "occupancy": {"required": True, 'regex': r'[0-9]+'},
    "max_occupancy": {"required": True, 'regex': r'[0-9]+'},
    "category_id": {"required": True, 'regex': r'[0-9]+'},
}