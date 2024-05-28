from app import app, db, Room


with app.app_context():
    db.create_all()
    
    rooms = [
        Room(room_number=101, room_type="Single"),
        Room(room_number=102, room_type="Single"),
        Room(room_number=103, room_type="Single"),
        Room(room_number=104, room_type="Single"),
        Room(room_number=105, room_type="Single"),
        Room(room_number=106, room_type="Single"),
        Room(room_number=107, room_type="Single"),
        Room(room_number=108, room_type="Single"),
        Room(room_number=109, room_type="Single"),
        Room(room_number=201, room_type="Double"),
        Room(room_number=202, room_type="Double"),
        Room(room_number=203, room_type="Double"),
        Room(room_number=204, room_type="Double"),
        Room(room_number=205, room_type="Double"),
        Room(room_number=206, room_type="Double"),
        Room(room_number=207, room_type="Double"),
        Room(room_number=301, room_type="Suite"),
        Room(room_number=302, room_type="Suite"),
        Room(room_number=303, room_type="Suite"),
        Room(room_number=304, room_type="Suite"),
        Room(room_number=305, room_type="Suite"),
    ]

    db.session.add_all(rooms)
    db.session.commit()