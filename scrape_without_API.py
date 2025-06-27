import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

MAX_TWEETS = 10

try:
    client = tweepy.Client(
        bearer_token=os.environ['TWITTER_BEARER_TOKEN'],
        wait_on_rate_limit=True  
    )
except KeyError as e:
    print(f"Missing environment variable: {e}")
    exit()

# Simplified query for Essential access tier
QUERY = '(earthquake OR tremor OR seismic) (Myanmar OR "Burma") lang:en -is:retweet'

try: 
    tweets = client.search_recent_tweets(
        query=QUERY,
        max_results=MAX_TWEETS,
        tweet_fields=["created_at", "public_metrics"]  # Note: 'geo' requires Elevated access
    )
    
    if tweets.data:
        for tweet in tweets.data:
            print("Tweet ID:", tweet.id)
            print("Created at:", tweet.created_at)
            print("Text:", tweet.text)
            print("Likes:", tweet.public_metrics['like_count'])
    else:
        print("No tweets found")
        
except tweepy.TweepyException as e:
    print(f"Twitter API error: {e}")
except Exception as e:
    print(f"General error: {e}")