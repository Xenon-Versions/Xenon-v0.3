import vars_setup
import funcs
import os
def send(user):
    funcs.saveTempData(user)
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'whatsSend.py')}")