from pymongo import MongoClient
import os
import time
from Power import Power

connection_string = os.getenv('MONGODB_PATH')
client = MongoClient(connection_string)

db_name = 'system_monitor'
collection_name = 'usage_data'

db = client[db_name]
collection = db[collection_name]

while True:
    power = Power()
    print(power.__dict__)
    collection.insert_one(power.__dict__)

    count = collection.count_documents({})
    if count > 3:
        oldest_log = collection.find_one(sort=[("timestamp", 1)])
        collection.delete_one({"_id": oldest_log["_id"]})
        print(collection.count_documents({}))

    time.sleep(1)
