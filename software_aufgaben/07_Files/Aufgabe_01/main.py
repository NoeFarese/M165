from pymongo import MongoClient
import gridfs
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['files']
fs = gridfs.GridFS(db)

path = input("File: ")
# /Users/noefarese/Documents/baum.jpeg

# Save
with open(path, 'rb') as file:
    file_id = fs.put(file, filename=os.path.basename(path))
print("File saved")


# Read
file = fs.get(file_id)
restore_path = os.path.join("..", file.filename) # eis directory höcher mit em gliiche file name

data = fs.get(file_id).read()
with open(restore_path, 'wb') as file:
    file.write(data)
print("File restored")