import os
import funcs

userLogin = os.getlogin()

def doAdmin(user):
    try:
        file = open(f"C:/Users/{userLogin}/adminCommands/{user[6:]}")
        os.system(f"python C:/Users/{userLogin}/adminCommands/{user[6:]}")
    except Exception as e:
        print(e)
        funcs.printAndSay("This device is not a Xenon-admin-device")