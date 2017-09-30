import markovify
import tweepy
import re
import sys
import random
from os import environ

consumer_key        = environ.get('CONSUMER_KEY')
consumer_secret     = environ.get('CONSUMER_SECRET')
access_token        = environ.get('ACCESS_TOKEN')
access_token_secret = environ.get('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_all_tweets(screen_name):
    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name, count=200)

    alltweets.extend(new_tweets)
    oldest = alltweets[-1].id - 1

    while (len(alltweets) < 1000 and len(new_tweets) > 0):            
        #all subsiquent requests use the max_id param to prevent duplicates
        new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
        
        #save most recent tweets
        alltweets.extend(new_tweets)
        
        #update the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1
        
    outtweets = [(tweet.text.encode("utf-8") + " ") for tweet in alltweets]
    outtweets = remove_retweets(outtweets)

    return outtweets

def get_rand_id(screen_name):
    alltweets = []

    new_tweets = api.user_timeline(screen_name = screen_name, count=20)

    alltweets.extend(new_tweets)
    rand_index = random.randint(0, len(alltweets)/2)

    while (alltweets[rand_index].text.startswith("RT")):   
        rand_index = random.randint(0, len(alltweets)/2)

    tweet_id = str(alltweets[rand_index].id)
    
    return tweet_id

def get_markov_tweet(screen_name):

    text = "".join(get_all_tweets(screen_name))

    # Build the model.
    text_model = markovify.Text(text)

    # Print three randomly-generated sentences of no more than 140 characters
    return text_model.make_short_sentence(140)

def remove_retweets(outtweets):
    for tweet in range(0,len(outtweets)):
        outtweets[tweet]= re.sub(r"http\S+", "",outtweets[tweet])

        if(outtweets[tweet].startswith("RT")):
            outtweets[tweet] = ""
        outtweets[tweet] = outtweets[tweet].replace("&lt;", "<");
        outtweets[tweet] = outtweets[tweet].replace("&gt;", ">");
        outtweets[tweet] = outtweets[tweet].replace("&amp;", "&");

    return outtweets

def check_handle(handle):
    try:
        api.user_timeline(screen_name = handle, count=1)
        return True
    except tweepy.TweepError as e:
        pass
    return False
