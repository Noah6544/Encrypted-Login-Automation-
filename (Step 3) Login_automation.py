"""
this step will use pyautogui to naviagate clicks to, for example, launch google, type gmail, then enter your password in seconds. 
you will have to setup your own clicks
"""
#an example is a function for logging into discord. I use functions for each application because i can run each separtely and organized better.

def discordin():
		# my click locations may be different than yours because of my resolution on my pc and the order I like to go in
    subprocess.Popen("C:\\Users\\user\\AppData\\Local\\Discord\\app-0.0.309\\Discord.exe")
    time.sleep(2)
    py.click(400, 490)
    py.typewrite(username)
    time.sleep(.05)
    py.click(423, 570)
    time.sleep(.05)
    py.typewrite(str(discordpass))
		# I DO NOT RECCOMEND USING "py.typewrite("enter")" because you can VERY EASILY enter your login information somewhere you dont want...like a live stream chat.....speaking from experience. do no put enter. just click on the login button if possible.
    py.click(497, 660)
