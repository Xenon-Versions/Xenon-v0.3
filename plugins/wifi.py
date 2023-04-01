import os

def wifiDisable():
    os.system("netsh wlan disconnect")

def wifiConnect(wifiName):
    os.system(f'netsh wlan connect "{wifiName}"')

def wifiList():
    os.system("netsh wlan show profiles")

def wifiHandler(user):
    userS = user.split(" ")
    subCommand = userS[1]
    if subCommand == "-connect":
        wifiName = user[14:]
        wifiConnect(wifiName)
    if subCommand == "-disable":
        wifiDisable()
    if subCommand == "-list":
        wifiList()