import pyautogui as py
import webbrowser
import subprocess
import time
from cryptography.fernet import Fernet

"""
This step will encrypt your passwords. run as many times as you have passwords to encrypt. Make another custom txt file, name it what you want, and replace all "programpass.txt" with "whateveryounamedit.txt" then everything should work
enter all information in variable starting with email.
!!!
you have to actually put your real password below. You can erase it after you run this program but you must enter it directly below. this sounds like a scam when i say it like this...but i'm not advanced enough to figure out how to grab passwords. wow this even more like a scam. its not tho just trying to make this code avaliable for anyone who might want to encrypt passwords.
""""
actualprogrampassword = "enter here"
Key = open("Key.txt","rb").read()
cipher_suite = Fernet(Key)
programpassfile = open("C:\\userdirectory\\programpass.txt","wb") #insert correct file path, adding "\\" for every directory change idk y 
encoded_text = cipher_suite.encrypt(b"actualprogrampassword") #encrypts your password entered above
programpassfile = programpassfile.write(encoded_text) #if it doesnt work add ".bytes()" ? i think. 
"""
#these two lines simply decrypt your password, you can then use these for the gui automation in the next step (click and typing)
programpassfile = cipher_suite.decrypt(programpassfile)
programpassfile = programpassfile.decode('utf-8')
"""
