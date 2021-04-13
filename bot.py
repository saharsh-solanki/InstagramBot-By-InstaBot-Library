import Credential

from instabot import Bot

import os

import time 

from random import * 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'






#Function For Proccess Methods
def Process_method():
    print(f"{bcolors.WARNING} !! Select Your Proccess !! ")
    print(f"""
    {bcolors.OKCYAN}
    1 : Follow Followers Of a User 
    2 : Approve Pending Follow  Requests 
    3 : unfollows users that don't follow you.
    4 : unfollows every from your account.
    """)
    Deliverymethod = int(input("Select A Method From Above Exp. 1 : "))
    if Deliverymethod == 1:
        print(f"{bcolors.WARNING} !! Proccess Started : Follow Follower Of A Instagram Accoount !! ")
        insta_username = input(f"{bcolors.OKGREEN} Enter Username Of The Account That You Want To Follow : ")
        followers = bot.get_user_followers(insta_username)
        for user in followers:
            if bot.follow(user) :
                pass
            else:
                pass
        # bot.follow_followers(insta_username)
        print(f"{bcolors.OKGREEN} Successfully Followed Everyone ")
        Process_method()
    elif Deliverymethod == 2:
        print(f"{bcolors.WARNING} !! Proccess Started : Approve Pending Follow Request !! ")
        bot.approve_pending_follow_requests()
        print(f"{bcolors.OKGREEN} Approved All Follow Request ")
        Process_method()
    elif Deliverymethod == 3:
        print(f"{bcolors.WARNING} !! Proccess Started : Unfollow Users That Don't Follow You !! ")
        bot.unfollow_non_followers()
        print(f"{bcolors.OKGREEN} Successfully Unfollowd The User Who Don't Follow You ")
        Process_method()
    elif Deliverymethod == 4:
        print(f"{bcolors.WARNING} !! Proccess Started : Unfollow EveryOne From Your Account  !! ")
        bot.unfollow_everyone()
        print(f"{bcolors.OKGREEN} Successfully Unfolloed Everyone ")
        Process_method()    
    else:
        print(f"{bcolors.FAIL}Invalid Method")
        print(f"{bcolors.OKGREEN} Successfully Followed Everyone ")
        Process_method()



print(f"{bcolors.OKGREEN}\n \n !! Welcome To Instagram Bot By Saharsh Solanki Paytm Badshah Youtube  !! \n \n")

print(f"{bcolors.ENDC}Trying To Login Please Wait")

if os.path.isfile(os.getcwd()+"/config/"+Credential.my_username+"_uuid_and_cookie.json"):
    os.remove(os.getcwd()+"/config/"+Credential.my_username+"_uuid_and_cookie.json")

bot = Bot(
            filter_users=False, 
            filter_private_users=False,
            follow_delay=10,
            max_follows_per_day = 10000,
            max_unfollows_per_day  = 10000,
            )

bot.login(username=Credential.my_username, password=Credential.my_password,force=True)



Process_method()

