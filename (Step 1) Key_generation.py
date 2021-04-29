import pyautogui as py
import webbrowser
import subprocess
import time
from cryptography.fernet import Fernet

"""
!!!
Only run this file 1 time. if you run it multiple times, then you might mess up the key generation. This code generates a key which decrypts other passwords. If you're having errors, try to come back here and start over. Wipe all files to start over.
!!!
"""

keyfile = open("Key.txt","w")
#generates key. if you run this file more than once, the #key will change and the password encryption will be messed up
key = Fernet.generate_key()
cipher_suite = Fernet(key)
#writes the key to a file to be used later. this key can be used for all passwords.
keyfile.write(str(cipher_suite))
keyfile.close()