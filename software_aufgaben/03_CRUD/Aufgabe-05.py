from pymongo import MongoClient

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client["restaurants"]
collection = db["restaurants"]


def search_restaurants(name=None, cuisine=None):
    search_filter = {}

    if name:
        search_filter['name'] = {'$regex': name, "$options": "i"}  # i für case-insensitive
    if cuisine:
        search_filter['cuisine'] = {'$regex': cuisine, "$options": "i"}

    results = collection.find(search_filter)
    return results


results = search_restaurants(name="Riv", cuisine="American")
for restaurant in results:
    print(restaurant)
