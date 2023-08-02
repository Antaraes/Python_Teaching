from PIL import Image

# Importing the StringIO module.
import requests
from io import BytesIO,StringIO
# get image sizes from user
# save as photo unique
imageURL = "https://images.unsplash.com/photo-1508921912186-1d1a45ebb3c1?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG98ZW58MHx8MHx8fDA%3D&w=1000&q=80"
r = requests.get(imageURL)

image = Image.open(BytesIO(r.content)) # png , svg
resized_Image = image.resize((600,400))
resized_Image.save("./assets/photo1" + str(resized_Image.size) + ".jpeg") # dynamic
