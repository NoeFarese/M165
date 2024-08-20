from pymongo import MongoClient
import os

connection_string = os.getenv('MONGODB_PATH')
client = MongoClient(connection_string)

dblist = client.list_database_names()
for db in dblist:
    print(db)