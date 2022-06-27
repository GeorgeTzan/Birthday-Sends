from instagrapi import Client
from classes import login,birthdayCheck,sendmessage
import time
import getpass
cl = Client()


USERNAME = input("Instagram username: ")
PASSWORD = getpass.getpass(prompt="Instagram password: ")
VRF_Code = input("Verification code: ") #if you don't have just leave it empty

login(USERNAME,PASSWORD,VRF_Code)

while True:
    while time.strftime("%H:%M:%S") != '00:00:00':
        time.strftime("%H:%M:%S")
    else:
        print ("sending..")
        id = birthdayCheck()
        print ("Messages Delivered!")
    time.sleep(86380)
    
