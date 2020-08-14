from twython import Twython
import requests
from io import BytesIO
from makevid import makevid
from os import environ

credentials = open('credentials.txt', 'r')

interval = 60

consumer_key = credentials.readline().strip()
consumer_secret = credentials.readline().strip()
access_key = credentials.readline().strip()
access_secret = credentials.readline().strip()

api = Twython(consumer_key, consumer_secret, access_key, access_secret)

mentions = api.get_mentions_timeline()
for mention in mentions:
    print(mention['user']['screen_name'])
