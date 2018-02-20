# Python:       Program for Mining Twitter Feed
# Author:       Sohail Shaikh
# Created:      19-Feb-2018
# Modified:     19-Feb-2018
# Script:       getTwitter-Feed.py

import tweepy
from tweepy import OAuthHandler
import json

file = open('twitoken.json', 'r')
ds = json.load(file)

consumer_key = ds['consumer_key']
consumer_secret = ds['consumer_secret']
access_token = ds['access_token_key']
access_secret = ds['access_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
api.verify_credentials()
s = tweepy.Cursor(api.home_timeline).items(6)

for status in s:
    print(status.id, "\t", status.created_at, "\t", status.text)

