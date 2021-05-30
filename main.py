import os
import time as t
import tweepy
from datetime import date
from dotenv import load_dotenv

# Interval for every 24 hours
INTERVAL = 60 * 60 * 24

# Loads the .env file for the credentials
load_dotenv()
# Credentials set in the .env file
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# BOBBY was released on February 23rd, 2021
f_date = date(2021, 3, 23)
l_date = date.today()
delta = l_date - f_date

# Infinite loop, tweet every day rest for 24 hours until the next day.
while True:
    api.update_status(
        "It has been {0} days since Bobby Schmurda has been out of prison and NOT released a song.".format(delta.days))
    t.sleep(INTERVAL)
