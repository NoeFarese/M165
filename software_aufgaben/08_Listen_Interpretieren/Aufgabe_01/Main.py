from PIL import Image, ImageDraw
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]
collection = db["neighborhoods"]

polygon_data = collection.find_one({'name': 'East Flatbush-Farragut'})['geometry']['coordinates']

image_size = (1500, 1500)
background_color = (255, 255, 255)

image = Image.new(mode="RGB", size=image_size, color=background_color)
draw = ImageDraw.Draw(image)


# Funktion zum Umwandeln von Geo-Koordinaten in Bildkoordinaten definieren
def map_coordinates(longitude, latitude):
    x = int((longitude + 73.94) * (image_size[0] / 0.02))
    y = int((40.65 - latitude) * (image_size[1] / 0.02))
    return x, y


# Polygone auf das Bild zeichnen
for polygon in polygon_data:
    mapped_polygon = [map_coordinates(lon, lat) for lon, lat in polygon]
    draw.polygon(mapped_polygon, outline="black", fill=None)


image.show()
