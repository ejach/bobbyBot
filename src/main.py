import math
import os
from datetime import date, datetime, timedelta
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


# Checks if the credentials entered are correct
def authenticate():
    if not api.verify_credentials():
        print('Authentication: FAILED')
        return False
    else:
        print('Authentication: OK')
        return True


def tweet():
    # BOBBY was released on February 23rd, 2021
    f_date = date(2021, 3, 23)
    l_date = date.today()
    delta = l_date - f_date
    api.update_status(
        "It has been {0} days since Bobby Shmurda has been out of prison and NOT released a song.".format(
            delta.days))
    print('Tweet has been sent! See you in 24h.')


# Calculates the amount of time left (in minutes) before 12am
def time_left():
    time_delta = datetime.combine(
        datetime.now().date() + timedelta(days=1), datetime.strptime("0000", "%H%M").time()
    ) - datetime.now()
    s = time_delta.seconds / 60
    return math.trunc(s)


# Every day at 12am, tweet
schedule.every().day.at("00:00").do(tweet)

# Infinite loop, tweets every day, rest for 24 hours until the next day.
# If executed twice within the 24 hour interval, it will notify the user how to proceed.
try:
    # Informs the user upon running the script how many minutes are left before the next tweet is sent
    print('There is {0} minutes until the next tweet is sent. Sit tight!'.format(time_left())) if authenticate() else \
        exit()
    while True:
        schedule.run_pending()
        time.sleep(1)
# Catch TweepError 187 and proceed accordingly.
# If upon execution the program catches error code 401, proceed accordingly
except tweepy.TweepError as err:
    if err.api_code == 187:
        print('Duplicate tweet detected. Please wait 24 hours before executing again, or just delete the newest tweet.')
    if err.api_code == 401:
        print('Error 401: Unauthorized. Please make sure your keys/credentials are correct and try again.')
