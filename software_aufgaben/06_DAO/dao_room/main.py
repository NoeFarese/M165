from room import Room
from dao_room import DaoRoom

dao_room = DaoRoom("mongodb://localhost:27017/")

# create room
room_create = Room("Pilatus", 12, True)
dao_room.create(room_create)

# read room
room_read = dao_room.read()
if room_read:
    print(room_read.name, room_read.seats, room_read.is_reservable)

# update room
room_read.seats = 15
dao_room.update(room_read)

room_read = dao_room.read()
if room_read:
    print(room_read.name, room_read.seats, room_read.is_reservable)


if room_read:
    dao_room.delete(room_read._id)
