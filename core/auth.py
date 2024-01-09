import tweepy
from core.config import ACCESS_KEY, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET

# Twitter authentication
auth = tweepy.OAuthHandler(ACCESS_KEY, ACCESS_SECRET)
auth.set_access_token(CONSUMER_KEY, CONSUMER_SECRET)
