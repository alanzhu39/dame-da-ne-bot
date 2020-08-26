
from twython import Twython
import requests
from io import BytesIO
from makevid import makevid
from os import environ

credentials = open('credentials.txt', 'r')

consumer_key = credentials.readline().strip()
consumer_secret = credentials.readline().strip()
access_key = credentials.readline().strip()
access_secret = credentials.readline().strip()

api = Twython(consumer_key, consumer_secret, access_key, access_secret)

f = open('files/02.png', 'wb')
base = open('base.jpg', 'rb')
f.write(base.read())
f.close()
base.close()
makevid()
video = open('final.mp4', 'rb')
response = api.upload_video(media=video, media_type='video/mp4')
api.update_status(status="Making memes since 2020. Follow the instructions in bio to get your own Dame Da Ne meme like the one below!",media_ids=[response['media_id']])
video.close()
