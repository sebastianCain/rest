from clarifai import rest
from clarifai.rest import ClarifaiApp
import tinify
from clarifai.rest import Image as ClImage

CLARIFAI_APP_ID = "Y8pZV9ZL3UxoCsTzeg-lK4zz6nJDJmZ0bt0xheJA"
CLARIFAI_APP_SECRET = "RtqGr7kvfCdiyzCRZsJ2ElqdsjJpreydSkTCZUO4"


#to make a request:

model = app.models.get('general-v1.3')
image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
model.predict([image])

#request response:

dict = response["output"][0]["data"]["concepts"]
keywords = []
for i in dict:
  keywords.append(i["name"])
  # i["value"] is the likelihood of the image relating to the

tinify.key = "N5bZsPRvTbuuTmdrXykaLC7WJPmnrW3N"

