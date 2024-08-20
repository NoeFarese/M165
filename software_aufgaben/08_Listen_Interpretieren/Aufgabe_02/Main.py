from PIL import Image, ImageDraw
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["restaurants"]
collection = db["neighborhoods"]

all_polygons = [polygon['geometry']['coordinates'][0] for polygon in collection.find()]


image_size = (800, 800)
background_color = (255, 255, 255)

image = Image.new(mode="RGB", size=image_size, color=background_color)
draw = ImageDraw.Draw(image)

