from pymongo import MongoClient
import gridfs
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['photo_album']
fs = gridfs.GridFS(db)


def add_photo_to_album(file_path, album_name):
    with open(file_path, 'rb') as file:
        file_id = fs.put(file, filename=os.path.basename(file_path), album=album_name)
    print(f"File {file_path} saved to album {album_name} with id {file_id}")


def get_photos_from_album(album_name, download_path):
    for grid_out in fs.find({"album": album_name}):
        photo_data = grid_out.read()
        restore_path = os.path.join(download_path, grid_out.filename)
        with open(restore_path, 'wb') as file:
            file.write(photo_data)
        print(f"File {grid_out.filename} restored to {restore_path}")


file_path = input("File to add: ")
album_name = input("Album name: ")
add_photo_to_album(file_path, album_name)

album_name = input("Album name to download: ")
download_path = input("Path to save photos: ") # /Users/noefarese/Downloads
get_photos_from_album(album_name, download_path)
