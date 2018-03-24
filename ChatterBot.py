{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyError",
     "evalue": "'consumer_key'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-8596b2d3c030>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;31m# Twitter API Keys\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     12\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 13\u001b[1;33m \u001b[0mconsumer_key\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0menviron\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'consumer_key'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     14\u001b[0m \u001b[0mconsumer_secret\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0menviron\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'consumer_secret'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m \u001b[0maccess_token\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mos\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0menviront\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'access_token'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Anaconda3\\lib\\os.py\u001b[0m in \u001b[0;36m__getitem__\u001b[1;34m(self, key)\u001b[0m\n\u001b[0;32m    667\u001b[0m         \u001b[1;32mexcept\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    668\u001b[0m             \u001b[1;31m# raise KeyError with the original key value\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 669\u001b[1;33m             \u001b[1;32mraise\u001b[0m \u001b[0mKeyError\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkey\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    670\u001b[0m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdecodevalue\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mvalue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    671\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'consumer_key'"
     ]
    }
   ],
   "source": [
    "# Dependencies\n",
    "import tweepy\n",
    "import json\n",
    "import numpy as np\n",
    "import os\n",
    "import time\n",
    "\n",
    "# Import and Initialize Sentiment Analyzer\n",
    "from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer\n",
    "analyzer = SentimentIntensityAnalyzer()\n",
    "\n",
    "# Twitter API Keys\n",
    "\n",
    "consumer_key=os.environ['consumer_key']\n",
    "consumer_secret=os.environ['consumer_secret']\n",
    "access_token=os.environt['access_token']\n",
    "access_token_secret=os.environ['access_token_secret']\n",
    "\n",
    "\n",
    "# Setup Tweepy API Authentication\n",
    "auth = tweepy.OAuthHandler(consumer_key, consumer_secret)\n",
    "auth.set_access_token(access_token, access_token_secret)\n",
    "api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())\n",
    "\n",
    "# Create a function that tweets\n",
    "def TweetOut(tweet_number):\n",
    "    api.update_status(\n",
    "        \"Can't stop. Won't stop. Chatting! This is Tweet #%s!\" %\n",
    "        tweet_number)\n",
    "\n",
    "\n",
    "# Create a function that calls the TweetOut function every minute\n",
    "counter = 0\n",
    "\n",
    "# Infinitely loop\n",
    "while(True):\n",
    "\n",
    "    # Call the TweetQuotes function and specify the tweet number\n",
    "    TweetOut(counter)\n",
    "\n",
    "    # Once tweeted, wait 60 seconds before doing anything else\n",
    "    time.sleep(60)\n",
    "\n",
    "    # Add 1 to the counter prior to re-running the loop\n",
    "    counter = counter + 1\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
