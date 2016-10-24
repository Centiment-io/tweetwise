'''
collect_tweets.py
Includes functions for retrieving tweets using Tweepy API

Created by Miles Luders
'''

import tweepy, tweetwise_config, datetime, uuid


def authenticate():
    # Get api credentials from config file 
    # (config file is placed in .gitignore for security purposes)
    consumer_key = tweetwise_config.CONSUMER_KEY
    consumer_secret = tweetwise_config.CONSUMER_SECRET
    access_token = tweetwise_config.ACCESS_TOKEN
    access_token_secret = tweetwise_config.ACCESS_TOKEN_SECRET
    
    # Connect to api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)
        
    
  
def get_latest_tweets(query, count):
    api = authenticate()
    public_tweets = [(tweet.author.screen_name, 
                                    tweet.text,
                                    tweet.created_at.isoformat())
                      for tweet in api.search(q=query, count=count, lang='en')]
    return public_tweets


def write_tweets_to_file(fname, tweets):
    with open(fname, 'a') as f:
        for t in tweets:
            for a in t:
                f.write(a+"\n")
            
            #f.write(str(uuid.uuid(4))
            f.write("\n")
    

if __name__ == '__main__':
    T = get_latest_tweets('bitcoin', 5)
    #write_tweets_to_file('output.txt', T)
    print(len(T))