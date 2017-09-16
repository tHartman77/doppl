import tweepy
import re
from random import randint
from os.path import exists
import sys

consumer_key 		= '***REMOVED***'
consumer_secret		= '***REMOVED***'
access_token 		= '***REMOVED***'
access_token_secret = '***REMOVED***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_all_tweets(screen_name):

	if exists(screen_name + ".txt") :
		sys.exit()

	alltweets = []

	new_tweets = api.user_timeline(screen_name = screen_name, count=200)

	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1

	while (len(new_tweets) > 0):
		print "getting tweets before %s" % (oldest)
			
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))

	outtweets = [(tweet.text.encode("utf-8") + " " + str(tweet.favorite_count) + " " + str(tweet.retweet_count)) for tweet in alltweets]

	f = open(screen_name + '.txt','w')
		
		for tweet in outtweets:

			print(tweet)
			tweet= re.sub(r"http\S+", "",tweet)
			print(type('') is str)

		  f.write(tweet + "\r\n")

	f.close()

	g = open(screen_name + '.txt','w')
	
	g.write(data)

	g.close()


	pass

if __name__ == '__main__':
	get_all_tweets("quit_cryan")