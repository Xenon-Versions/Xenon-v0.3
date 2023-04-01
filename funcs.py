import pyttsx3
import vars_setup
from xenonData import myInfo
import pickle
import os
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

engine = pyttsx3.init()
engine.setProperty("rate",180)

def saveTempData(data):
    file = open(vars_setup.newPath(vars_setup.dataBasePath,'tempdata.tem'),"w")
    file.write(data)

def printAndSay(text):
    passw = True
    print(f"{vars_setup.DevInfo.assistantName(passw)}: {text}")
    user = vars_setup.Personal()
    if user.speech() == "on":
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0.0, None)
        engine.say(text)
        engine.runAndWait()
    else:
        pass

def loadAlias():
    file = open(vars_setup.newPath(vars_setup.dataBasePath,"alias.lock"),"rb")
    alias = pickle.load(file)
    file.close()
    return alias

def addAlias(aliasName,aliasContent,curretnAlias):
    curretnAlias[aliasName] = aliasContent
    file = open(vars_setup.newPath(vars_setup.dataBasePath,"alias.lock"),"wb")
    pickle.dump(curretnAlias,file)
    file.close()

def removeAlias(aliasName,currentAlias):
    currentAlias.pop(aliasName)
    file = open(vars_setup.newPath(vars_setup.dataBasePath,"alias.lock"),"wb")
    pickle.dump(currentAlias,file)
    file.close()

def listAlias(currentAlias):
    cnt = 0
    for i in currentAlias:
        print(f"Alias [{cnt}]: [{i}]")
        cnt += 1

def resetAlias(currentAlias):
    currentAlias.clear()
    file = open(vars_setup.newPath(vars_setup.dataBasePath,"alias.lock"),"wb")
    pickle.dump(currentAlias,file)

def getNum(method):
    def pic():
        path = vars_setup.picPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Photo-","")
            files[cnt] = files[cnt].replace(".jpg","")
            cnt += 1
        try:
            lFilenum = int(files[-1])
        except:
            lFilenum = 0
        return lFilenum+1

    def vid():
        path = vars_setup.newPath(vars_setup.dataBasePath,"Videos")
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Video-","")
            files[cnt] = files[cnt].replace(".avi","")
            cnt += 1
        try:
            lFilenum = int(files[-1])
        except:
            lFilenum = 0
        return lFilenum+1

    def logo():
        path = vars_setup.logoPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Logo-","")
            files[cnt] = files[cnt].replace(".png","")
            cnt += 1
        try:
            lFilenum = int(files[-1])
        except:
            lFilenum = 0
        return lFilenum+1

    def logoCat():
        path = vars_setup.catPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Catlog-","")
            cnt += 1
        try:
            lFilenum = int(files[-1])
        except:
            lFilenum = 0
        return lFilenum+1

    def ss():
        path = vars_setup.ssPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("ScreenShot-","")
            files[cnt] = files[cnt].replace(".png","")
            cnt += 1
        try:
            lFilenum = int(files[-1])
        except:
            lFilenum = 0
        return lFilenum+1

    numDict = {
        1: pic,
        2: vid,
        3: logo,
        4: logoCat,
        5: ss
    }
    if method in numDict:
        num = numDict[method]()
        return num

def printAndSayGPT(text):
    user = vars_setup.Personal()
    print(f"ChatGPT: {text}")
    if user.speech() == "on":
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None
        )
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0.0, None)
        engine.say(text)
        engine.runAndWait()
    else:
        pass