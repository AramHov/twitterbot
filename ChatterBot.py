# Dependencies

import tweepy
import json
import time
import os
import random
# Twitter API Keys

consumer_key=os.environ['consumer_key']
consumer_secret=os.environ['consumer_secret']
access_token=os.environt['access_token']
access_token_secret=os.environ['access_token_secret']


# Twitter credentials
auth = tweepy.OAuthHandler(Consumer_Key, Consumer_Secret)
auth.set_access_token(Access_Token, Access_Token_Secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Quotes to Tweet
happy_quotes = [
    "hello. - Ralph Waldo Emerson",
    "usually about as happy as they make their minds up to be. - Abraham Lincoln",
    "hink, what you say, and what you do are in harmony. - Mahatma Gandhi",
    "Cears. Count your life by smiles, not tears. - John Lennon",
    "Happin- Charles M. Schulz",
    "The hdepends upon the quality of your thoughts. - Marcus Aurelius",
    "Now andin our pursuit of happiness and laume Apollinaire"]


# Create function for tweeting
def HappyItUp():

    # Tweet a random quote
    api.update_status(random.choice(happy_quotes))

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
while(True):
    HappyItUp()
    time.sleep(60)
