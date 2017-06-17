"""
@description:Este script descarga los comentarios de las personas que hacen mension a la empresas que investigaremos
mediante una franja de tiempo(timeline), seran 30 empresas que se estudiaran  y se los clasificara por categorias
@autor : Kevin Andres Ortiz
@adicional : Los datos se guardarn en una base en mongodb
empresas :Claro
          netlife
          tvcable
          movistar
          cnt
          directt
"""

import tweepy
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/movistar_timeline_db'

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET=""

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api = tweepy.API(auth,wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)

cliente = MongoClient(MONGO_HOST)

db = cliente.movistar_timeline_db

try:
    for tweet in tweepy.Cursor(api.search,q="").items():
        if db.news.find_one({'text':tweet.text})==None:
            timelineUser = {'text':tweet.text,'id':tweet.id,'created_at':tweet.created_at,
                            'screen_name':tweet.author.screen_name,'author_id':tweet.author.id}
            db.news.save(timelineUser)
except tweepy.error.TweepError:
    print "error en la red"
except UnicodeDecodeError:
    pass

