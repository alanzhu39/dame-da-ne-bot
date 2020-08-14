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

while True:
    mentions = api.get_mentions_timeline()[::-1]
    recents = [status['in_reply_to_status_id'] for status in api.get_user_timeline()]
    curr = None
    for status in mentions:
        if status['id'] not in recents:
            texts = [hashtag['text'] for hashtag in status['entities']['hashtags']]
            if 'DameDaNeMe' in texts:
                curr = status
                break
    if curr is not None:
        print('success')
        print(curr['id'])
        f = open('files/02.png', 'wb')
        f.write(requests.get(curr['user']['profile_image_url_https']).content)
        f.close()
        makevid()
        video = open('final.mp4', 'rb')
        response = api.upload_video(media=video, media_type='video/mp4')
        api.update_status(status="@{} Here is your personally generated meme! I am a bot.".format(curr['user']['screen_name']), media_ids=[response['media_id']], in_reply_to_status_id=curr['id'])
    break
    time.sleep(interval)
