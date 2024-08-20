from pymongo import MongoClient
import bson

connection_string = "mongodb+srv://dbAdmin:96YCW4OkpxEIQefg@cluster0.ostytiv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(connection_string)

dblist = client.list_database_names()

if not dblist:
    print("No Database")
else:
    print("Databases")
    for db in dblist:
        print("- " + db)

    selected_db = input("Select Database: ")

    if selected_db in dblist:
        print(selected_db)
        db = client[selected_db]
        print("\nCollections")

        for collection in db.list_collection_names():
            print("- " + collection)

        selected_collection = input("Select Collection: ")

        if selected_collection in db.list_collection_names():
            print(selected_db + "." + selected_collection)
            print("Documents")

            collection = db[selected_collection]
            for document in collection.find({}, {"_id": 1}):
                print(" -", document["_id"])

            selected_document_id = input("\nSelect Document: ")
            document_id = bson.ObjectId(selected_document_id)
            document = collection.find_one({"_id": document_id})

            if document:
                print(selected_db + "." + selected_collection + "." + str(selected_document_id))
                for key, value in document.items():
                    print(key + ":", value)
                input("\nPress any button to return")

            else:
                print("Document not found")
                input("\nPress any button to return")
        else:
            print("Collection does not exist")
            input("\nPress any button to return")
    else:
        print("Database does not exist")
        input("\nPress any button to return")
