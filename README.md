# Encrypted-Login-Automation-
this is a script that I'm making in order to automatically sign in and out of spotify, discord, and google while encrypting the passwords and storing them on your pc. I'm trying to structure it so that it can be easily expanded when I have other sites to sign into.  
## VERSION
### First commit (2/12/2021)
- Well. I'm not sure what I'm doing. I've been coding for a couple of hours and have only managed to figure out how to encrypt/decrypt files while writing them to a file. It works when trying to sign in and out of discord. It also works signing out of google, havent worked on spotify yet.
### Completed
- I've managed to encrypt strings, store them on pc, decrypt bytes, convert to string, print out as text. 
- Managed to sign into discord and out of discord and ou of google autonomously. 
### Issues
- Sometimes the discord clicks register to logout and sometimes it doesnt. Right now the fix is just to increase the time.sleep() to a little more just in case it was clicking too fast, which is working.
- When trying to sign out, in this order: discordout(); googleout(), Google opens up before discord. Not sure why. hopefull will fix later. This is a personal project mainly and Im just posting for ego and im bored. so im not really trying to fix this as a program to be used by a lot of people.
### ToDo
- fix a lot of things. 
- My main problem is with creating a function that would be able to create encrypted files and decrypt them (call this encryptyer/decrypeter) to be used in my spotify function. I think i'm overthinking it but I'm not sure how I would get an argument in my encrypter() to be used in another function. Especially because you cant declare something Global if it's a parameter. 
- I will try to add a temporary variable that stores the information for each time it encrypts/decrypts. temp bcz I want to be able to run it multiple times without wasting so much compiling time and make many encrypted things in the future.
- Because I'm having trouble wrapping my head around making the files, opening the files, generating a key (making sure not to run it more than once to avoid generating a key that doesn't work for a password), I'm instead going to try to make diffferent .py files. Each labeled a different step with instructions on how to use each. This is supposed to be helpful for anyone wanting to create encrypted passwords without having to do much.
