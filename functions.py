
import pyautogui as py
import webbrowser
import subprocess
import time
from cryptography.fernet import Fernet

"""
#encrypting password
discordpassfile = open("discordpass.txt","w")
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"")
decoded_text = cipher_suite.decrypt((encoded_text))
discordpassfile.write(str(encoded_text))
discordpassfile.close()
"""


#VARIABLES
googlepass = None
email = ""
discordkey = open("discordkey.txt","rb")
key = bytes(discordkey.read())
discordkey.close()
cipher_suite = Fernet(key)
discordpassfile = open("discordpass.txt","rb")
discordpass = discordpassfile.read()
discordpass = cipher_suite.decrypt(discordpass)
discordpass = discordpass.decode('utf-8')
googlepass = ""
googlekey = ""
googlepassfile = open("googlepass.txt",)
googlepasstxt = "googlepass"

#only run this once, if you need to run it again, you'll have to delete your file because it generates a new key each time.
def encryptpassword(programpass,programkey,programpassfile,programpasstxt,passwordfrfr):
    key = Fernet.generate_key()
    programkey = open(programkey + ".txt", "wb")
    programkey.write(key) #if it doesnt work add bytes() here
    programkey.close()
    programkey = open(programpass + ".txt" + ".txt","rb")
    key = programkey.read() #if it doesnt work add bytes() here
    programkey.close()
    cipher_suite = Fernet(key)
    encrypt = cipher_suite.encrypt(b'passwordfrfr')
    programpassfile = open(programpasstxt + ".txt", "wb")
    programpassfile.write(encrypt)
    programpass.close()
    #todo add a global temp variable fore each so that you can assign it to an outside variable each time the fucntion is reused? idk if this will work but im done for today.

def decryptpassword(programkey,programpassfile,programpass,programpasstxt):
    programkey = open(programkey +".txt", "rb")
    key = programkey.read()
    programkey.close()
    cipher_suite = Fernet(key)
    programpassfile = open(programpasstxt + ".txt", "rb")
    programpass = programpassfile.read()
    programpass = cipher_suite.decrypt(programpass)
    programpass = programpass.decode('utf-8')
    print(programpass)

#completed
def discordin():
    subprocess.Popen("C:\\Users\\user\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe")
    time.sleep(2)
    py.click(400, 490)
    py.typewrite(username)
    time.sleep(.05)
    py.click(423, 570)
    time.sleep(.05)
    py.typewrite(str(discordpass))
    py.click(497, 660)



#coimplete
def discordout():
    subprocess.Popen("C:\\Users\\User\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe")
    time.sleep(1)
    py.click(300, 1016)
    time.sleep(1)
    py.click(503, 962)
    time.sleep(.7)
    py.click(1100, 570)
    time.sleep(1)
    
#incomplete
def googlein():
    subprocess.Popen("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
    time.sleep(1)
    py.typewrite("google.com")
    py.press("enter")
    time.sleep(.5)
    py.click(1860,94)
    py.click(839,437)
    py.typewrite()
    #1854 56
    #1695 460

def googleout():
    print(opengoogle)
    time.sleep(.7)
    py.typewrite("google.com")
    py.press("enter")
    time.sleep(1)
    py.click(1883, 96)
    time.sleep(.1)
    py.click(1734, 459)


#incomplete
def spotify():
    print("1")
    subprocess.Popen("C:\\Users\\User\\AppData\\Roaming\\Spotify")
    print("2")