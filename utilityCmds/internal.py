import os

def commandRuner(user):
    command = user[4:]
    os.system(command)