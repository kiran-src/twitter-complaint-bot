import os

from Tweet import Tweet
from SpeedTest import SpeedTest

twitter_url = "https://www.twitter.com"
speedtest_url = "https://www.speedtest.net"
PROMISED_DOWN = 25
PROMISED_UP = 5
t_pass = os.environ.get("TWITTER_PASS")
t_email = os.environ.get("TWITTER_EMAIL")
t_user = os.environ.get("TWITTER_USER")

# st = SpeedTest()
# a = st.get_speed()
tweet = Tweet()
tweet.login(t_pass, t_email, t_user)
tweet.speed_tweet()
