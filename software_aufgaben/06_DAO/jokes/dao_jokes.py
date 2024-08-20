from pymongo import MongoClient
from jokes.joke import Joke
from bson import ObjectId


class DaoJokes:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.col = MongoClient(connection_string)["jokes"]["jokes"]

    def insert(self, joke):
        if joke._id is None:
            joke._id = ObjectId()
        self.col.insert_one(joke.__dict__)

    def get_category(self, category):
        joke_data = self.col.find_one({"category": category})
        if joke_data:
            joke = Joke(**joke_data)
            return joke
        return None

    def delete(self, joke):
        result = self.col.delete_one({"_id": ObjectId(joke._id)})
        return result.deleted_count
