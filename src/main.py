import os
from datetime import date
import time

import schedule
import tweepy
from dotenv import load_dotenv

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


def tweet():
    # BOBBY was released on February 23rd, 2021
    f_date = date(2021, 3, 23)
    l_date = date.today()
    delta = l_date - f_date
    api.update_status(
        "It has been {0} days since Bobby Shmurda has been out of prison and NOT released a song.".format(
            delta.days))
    print('Tweet has been sent! See you in 24h.')


# Every day at 12am, tweet
schedule.every().day.at("00:00").do(tweet)

# Infinite loop, tweets every day, rest for 24 hours until the next day.
# If executed twice within the 24 hour interval, it will notify the user how to proceed.
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
# Catch TweepError 187 and proceed accordingly.
except tweepy.TweepError as err:
    if err.api_code == 187:
        print('Duplicate tweet detected. Please wait 24 hours before executing again, or just delete the newest tweet.')
