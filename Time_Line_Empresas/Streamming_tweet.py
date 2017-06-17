import tweepy
import json
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/'

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET=""

WORDS = ['','','']

class StreamListener(tweepy.StreamListener):

    def on_connect(self):
        print("conectado al streamming api")

    def on_error(self, status_code):
        print("Un error ha ocurrido " + repr(status_code))
        return False

    def on_data(self, raw_data):
        try:
            cliente = MongoClient(MONGO_HOST)

            db = cliente.base_de_datos

            datajson = json.loads(raw_data)

            creado = datajson['created_at']

            print("Tweet collected at" + str(creado))

            db.data_twitter.insert(datajson)

        except Exception as e:
            print (e)



auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True,wait_on_rate_limit_notify=True))
streammer = tweepy.Stream(auth=auth,listener=listener)
print("haciendo streamming"+str(WORDS))
streammer.filter(track=WORDS,async=True)




