from instagrapi import Client
import time
cl = Client()

def login(USERNAME,PASSWORD,VRF_Code):
    if VRF_Code != "":
        cl.login(USERNAME, PASSWORD, verification_code= VRF_Code)
    else:
        cl.login(USERNAME, PASSWORD)
def birthdayCheck():
    fileName = open('birthdays.txt', 'r')
    today = time.strftime('%m%d')
    flag = 1
    while flag != -1:
            for line in fileName:
                if today in line:
                    line = line.split(' ')
                    try:
                        sendmessage(line[1].replace('\n', ""))
                    except:
                        print ("Sending Failed.. Skipping..")
            if fileName.readline() == '':
                flag = -1
    
def sendmessage(id):
    id = cl.user_id_from_username(str(id))
    id = int(id)
    for i in range(5):
        cl.direct_send('Happy Birthday', user_ids=[id])
