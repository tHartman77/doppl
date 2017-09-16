import tweepy
from random import randint
from os.path import exists

consumer_key 		= '***REMOVED***'
consumer_secret		= '***REMOVED***'
access_token 		= '***REMOVED***'
access_token_secret = '***REMOVED***'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

def get_all_tweets(screen_name):
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

	outtweets = [(tweet.text.encode("utf-8") + " " + str(tweet.favorite_count) + " " + str(tweet.retweet_count) + "\n") for tweet in alltweets]

	if not exists("home/Documents/Twitter/doppel/" + screen_name + ".txt") :
		f = open(screen_name + '.txt','w')
		
		for tweet in outtweets:
			f.write(tweet)

		f.close()

	pass

if __name__ == '__main__':
	get_all_tweets("quit_cryan")