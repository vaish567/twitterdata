import tweepy
import time

auth = tweepy.OAuthHandler('VYOgi7Xmv99XOc8A4KO1Zj1fi','iavfQGBZShNm6J38sJ3p2TbiQpPZQbH8yjGGsmc2p9jXrCUwhd')


auth.set_access_token('1283694156317986819-BpINC7qOZaTnGlCzsBCGCh5c9EcVdX','BNT9X0LaW2xbYtMMIMrL8zr3cbLTIxR897Sq0rAN4W8LI')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)


user = api.me()

search = 'Javascript'
nrTweets = 100

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
            print(e.reason)
    except StopIteration:
        break  

user = api.me()

search = 'Covid-19'
nrTweets = 100
for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Retweet OP')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
            print(e.reason)
    except StopIteration:
        break  