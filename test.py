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

video = open('final.mp4', 'rb')
response = api.upload_video(media=video, media_type='video/mp4')
api.update_status(status="Here is your personally generated meme! I am a bot.", media_ids=[response['media_id']])
video.close()