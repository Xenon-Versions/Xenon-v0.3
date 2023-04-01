import os
import vars_setup
import funcs
def rma(user):
    funcs.saveTempData(user)
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'rma.py')}")