import math
from pymongo import MongoClient

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

db = client['restaurants']
collection = db["restaurants"]
le_perigord = collection.find_one({"name": "Le Perigord"})
le_perigord_coordinates = le_perigord["address"]["coord"]
restaurants = collection.find({"name": {"$ne": "Le Perigord"}})
closest_restaurant = None
min_distance = None

for restaurant in restaurants:
    location = restaurant["address"]["coord"]
    if location:
        distance = math.hypot((location[0] - le_perigord_coordinates[0]), (location[1] - le_perigord_coordinates[1]))

        if not min_distance:
            min_distance = distance
            closest_restaurant = restaurant

        if distance < min_distance:
            closest_restaurant = restaurant
            min_distance = distance

print(closest_restaurant["name"])
