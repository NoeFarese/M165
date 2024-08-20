from pymongo import MongoClient

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
db = client['restaurants']

query = [
    {
        "$project": {
            "name": 1,
            "avg_rating": { "$avg": "$grades.score" }
        }
    },
    { "$sort": { "avg_rating": -1 } },
    { "$limit": 3 }
]

top_restaurants = db.restaurants.aggregate(query)

for restaurant in top_restaurants:
    print(restaurant["name"], "-", "Durchschnittliches Rating:", restaurant["avg_rating"])
