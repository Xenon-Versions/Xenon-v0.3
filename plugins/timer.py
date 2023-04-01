import os
import funcs
import vars_setup

def timer(user):
    userS = user.split(" ")
    num = userS[1]
    funcs.saveTempData(num)
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'timer.py')}")
