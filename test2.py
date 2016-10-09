
from clarifai.client import ClarifaiApi



app = ClarifaiApi()

result = app.tag_image_urls('http://images.hellogiggles.com/uploads/2015/11/30/o-DAWSONS-CREEK-REUNION-facebook.jpg')

print(result)