from pymongo import MongoClient
from room import Room


class DaoRoom:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.col = MongoClient(connection_string)["buildings"]["rooms"]

    def create(self, room):
        self.col.insert_one(room.__dict__)

    def read(self):
        room = Room(**self.col.find_one())
        return room

    def update(self, room):
        self.col.update_one({"_id": room._id}, {"$set": room.__dict__})

    def delete(self, _id):
        return self.col.delete_one({"_id": _id})
