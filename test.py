'''
Test script, used to connect to api and get latest tweets

Created by Miles Luders
'''

import tweepy, tweetwise_config


def authenticate():
    # Get api credentials from config file (for security purposes)
    consumer_key = tweetwise_config.CONSUMER_KEY
    consumer_secret = tweetwise_config.CONSUMER_SECRET
    access_token = tweetwise_config.ACCESS_TOKEN
    access_token_secret = tweetwise_config.ACCESS_TOKEN_SECRET
    
    # Connect to api
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth)

  
def get_latest_tweets(query):
    api = authenticate()
    public_tweets = [(tweet.author.screen_name, tweet.text) for tweet in api.search(q=query, count=100)]
    return public_tweets
    

if __name__ == '__main__':
    print("Hello World!")
    #print(get_latest_tweets('bitcoin'))    