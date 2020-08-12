import tweepy
from os import environ

credentials = open('credentials.txt', 'r')

interval = 60

consumer_key = credentials.readline().strip()
consumer_secret = credentials.readline().strip()
access_key = credentials.readline().strip()
access_secret = credentials.readline().strip()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

mentions = api.mentions_timeline()
for status in mentions:
    print(status.entities['hashtags'])
    if 'DameDaNeBot' in status.entities['hashtags']['text']:
        print('success')
"""
while True:
    mentions = api.mentions_timeline()
    recents = [status.in_reply_to_status_id for status in api.user_timeline('DameDaNeMe')]
    curr = None
    for status in mentions:
        if status.id not in recents:
            curr = status
            break
    if curr == None:
        continue
    time.sleep(interval)
"""
