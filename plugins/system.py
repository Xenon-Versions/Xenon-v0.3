import vars_setup
import os

def his():
    os.startfile(vars_setup.newPath(vars_setup.dataBasePath,'history.txt'))
def errRep():
    os.startfile(vars_setup.newPath(vars_setup.dataBasePath,'error-report.txt'))

def internal(user):
    subCommand = user.split(" ")[1]
    if subCommand == "-ss":
        os.startfile(vars_setup.ssPath)
    if subCommand == "-video":
        os.startfile(vars_setup.newPath(vars_setup.dataBasePath,"Videos"))
    if subCommand == "-pic":
        os.startfile(vars_setup.picPath)
    if subCommand == "-dp":
        os.startfile(vars_setup.logoPath)
    if subCommand == "-catlog":
        os.startfile(vars_setup.catPath)