import praw
import config

def bot_login():
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "MK Buying Notification v1.0")
	return r

def run_bot(r):
	subreddit = r.subreddit("mechanicalkeyboards+mechmarket")
	for title in subreddit.stream.submissions():



r = bot_login()
print(r.user.me())