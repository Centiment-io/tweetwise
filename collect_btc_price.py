'''
collect_tweets.py
Includes functions for retrieving and storing bitcoin prices

Created by Miles Luders
'''

import requests


def get_btc_info():
    try:
        url = 'https://api.cryptonator.com/api/ticker/btc-usd'
        response = requests.get(url)
        return response.text
    except:
        return None
    

def write_price_to_file(price, fname):
    if price:
        try:
            with open(fname, 'a') as f:
                f.write(price+"\n")
            print("Successfully wrote btc price")
        except:
            print("Error writing price to '" + fname + "'")
    else:
        print("No tweet to write")
  
if __name__ == "__main__":          
    p = get_btc_info()
    write_price_to_file(p, 'prices.txt')