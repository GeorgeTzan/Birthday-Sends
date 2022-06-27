from instagrapi import Client
from progressbar import progressbar
import time
cl = Client()
import threading

def login(USERNAME,PASSWORD,VRF_Code):
    if VRF_Code != "":
        cl.login(USERNAME, PASSWORD, verification_code= VRF_Code)
    else:
        cl.login(USERNAME, PASSWORD)
def birthdayCheck():
    fileName = open('birthdays.txt', 'r')
    today = time.strftime('%m%d')
    flag = -1
    global line
    while flag == -1:
            for line in fileName:
                if today in line:
                    line = line.split(' ')
                    try:
                        sendmessage(line[1].replace('\n', ""))
                    except:
                        print ("Sending Failed.. Skipping..")
            if fileName.readline() == '':
                flag = 0
    

def updateFollows():
    followers = cl.user_following(cl.user_id)
    for user_id in followers.keys():
        if user_id in cl.user_followers(cl.user_id):
            with open("following.txt", "at") as fls:
                fls.write(f"{user_id}\n")
def sendmessage(id):
    id = cl.user_id_from_username(str(id))
    id = int(id)
    for i in range(5):
        cl.direct_send('xronia polla', user_ids=[id])


def lista(count):
    with open("lastPosition.txt", "r") as fls:
        for line in fls:
            count = count + 1
    return count
def listavath(count):
    with open("bathmoi.txt", "r") as fls:
        for line in fls:
            count = count + 1
    return count
def multipleLista(count):
    with open("multiplePositions.txt", "r") as fls:
        for line in fls:
            count = count + 1
        return count
def deleteFollowingList():
    with open("following.txt","w") as fls:
        fls.write("")
        
def unfollowing(count):
    with open("following.txt", "r") as fls:
        if len(fls.read()) != 0:
            fls.seek(0)
            for users in range(count):
                user_id = fls.readline()
                user_id = user_id.replace("\n", "")
                if user_id in cl.user_followers(cl.user_id):
                    print(user_id)
                    print (f"se kanei follow ({cl.username_from_user_id(user_id)}) \n")
                else:
                    print (f"den einai se kanei follow ({cl.username_from_user_id(user_id)})")
                    print(user_id)
                    print()
                    
        else:
            updateFollows()
            unfollowing(count)
    
