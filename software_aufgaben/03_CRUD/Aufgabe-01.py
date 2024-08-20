from pymongo import MongoClient

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client['restaurants']

districts = db.restaurants.distinct("borough")
for district in districts:
    print(district)