'''
format_tweets.py
Includes methods for processing raw tweet data

Created by Miles Luders
'''
import collect_tweets


def remove_excess_whitespace(tweet_body):
    return ' '.join(tweet_body.split())
    

#def hash_tweet():



if __name__ == '__main__':
    print("hello")
    T = collect_tweets.get_latest_tweets('bitcoin', 2)
    for t in T:
        print(remove_excess_whitespace(t[1])+"\n")
    
