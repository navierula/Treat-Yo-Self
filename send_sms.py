

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
#import giphy stuff
import urllib,json
# Find these values at https://twilio.com/user/account
account_sid = "AC4b2a2b012ac5fa1f5f299f95a2ec0cb2"
auth_token = "cb422fa16b987043ed71eba7cf30f3c6"
client = TwilioRestClient(account_sid, auth_token)


data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=funny").read())
#message = client.messages.create(to="+13236278306", from_="+13233100654", body="Hello there!")
link = data["data"]["image_original_url"]
message = client.messages.create(to="+13236278306", from_="+13233100654",
                                     media_url=link)
