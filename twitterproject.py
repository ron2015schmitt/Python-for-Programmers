import sys
import twitter

# put actual credentials here
api = twitter.Api(consumer_key='xxx',
                  consumer_secret='xxx',
                  access_token_key='xxx',
                  access_token_secret='xxx')


print("\n\n\nCredentials ")
try:
    credentials = api.VerifyCredentials()
    print(credentials)
except:
    print('credntials failed\n')
    sys.exit()

print("\n\n\nFollowing")
try:
    following = api.GetFriends()
    print(following)
except:
    print('following failed\n')

print("\n\n\nFirst Following User")
user=following[0].AsDict()
print(type(user))
print(user)

print("\nname=@"+user["screen_name"]+"\n\n")

tweet="This is a late night tweet from a bot"
print("post a tweet: `"+tweet+"'.")
try:
    print(api.PostUpdate(tweet))
except:
    print('post of tweet failed')

