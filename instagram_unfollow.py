from instabot import Bot
from time import sleep 
from random import randint 

bot = Bot()
username = 'Your_instagram_account_username'
password = 'Corresponding_password'

bot.login(username=username, password=password)

non_followers = set(bot.following)-set(bot.followers)
# print(len(non_followers))

for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
        sleep(randint(6, 12))

    except Exception as e:
        # print(e)
        sleep(randint(30, 300))