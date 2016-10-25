'''
collect_tweets.py
Includes functions for retrieving and storing tweets

Created by Miles Luders
'''

import tweepy, tweetwise_config, datetime, uuid


def authenticate():
    try:
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
    except:
        print("Failed to authorize Tweepy.")
        return None
   
  
def get_latest_tweets(query, count):
    public_tweets = []
    
    api = authenticate()
    if (api):        
        try:
            public_tweets = [(tweet.author.screen_name, 
                          tweet.text,
                          tweet.created_at.isoformat())
                          for tweet in api.search(q=query, count=count, lang='en')]
        except:
            print("Tweepy request failed.")
    
    return public_tweets


def write_tweets_to_file(fname, tweets):
    if len(tweets) == 0:
        print("Number of tweets to write is zero.")
        return

    try:
        with open(fname, 'a') as f:
            for t in tweets:
                for a in t:
                    f.write(a+"\n")
            
                #f.write(str(uuid.uuid(4))
                f.write("\n")
                
        print("Successfully wrote", len(tweets), "tweets")
    except:
        print("Error writing tweets to '" + fname + "'")
    

if __name__ == '__main__':
        d = datetime.datetime.now()
        print("Getting tweets... (", d, ")")
        T = get_latest_tweets('bitcoin', 11)
        write_tweets_to_file('output.txt', T)
