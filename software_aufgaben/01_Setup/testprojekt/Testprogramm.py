from pymongo import MongoClient

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)
# print(client.server_info())

dblist = client.list_database_names()

for db in dblist:
    print(db)

# traffic sollte schon existieren
if "traffic" in dblist:
    print("Traffic existiert bereits.")
    db = client["traffic"]
    collist = db.list_collection_names()

    for col in collist:
        print("collection name: " + col)
else:
    print("Traffic existiert nicht.")
    db = client["traffic"]
    print("Traffic-Datenbank erstellt.")
