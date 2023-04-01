import os

import pyttsx3
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import vars_setup

engine = pyttsx3.init()
engine.setProperty("rate", 180)


def saveTempData(data):
    file = open(vars_setup.newPath(vars_setup.dataBasePath, 'tempdata.tem'), "w")
    file.write(data)


def printAndSay(text):
    user = vars_setup.Personal()
    print(f"{vars_setup.DevInfo.assistantName(passw=True)}: {text}")
    if user.speech() == "on":
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevel(0.0, None)
        engine.say(text)
        engine.runAndWait()
    else:
        pass

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

def alert(title, message):
    import tkinter

    wn = tkinter.Tk()
    wn.geometry("300x100")
    wn.title(title)

    text = tkinter.Label(
        wn,
        text=message,
        pady=25
    )
    close = tkinter.Button(
        wn,
        text="Close",
        command=wn.destroy,
        height=1,
        width=10
    )

    text.pack()
    close.pack()

    wn.mainloop()


def getNum(method):
    def pic():
        path = vars_setup.picPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Photo-","")
            files[cnt] = files[cnt].replace(".jpg","")
            cnt += 1
        lFilenum = int(files[-1])
        return lFilenum+1

    def vid():
        path = vars_setup.newPath(vars_setup.dataBasePath,"Videos")
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Video-","")
            files[cnt] = files[cnt].replace(".avi","")
            cnt += 1
        lFilenum = int(files[-1])
        return lFilenum+1

    def logo():
        path = vars_setup.logoPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Logo-","")
            files[cnt] = files[cnt].replace(".png","")
            cnt += 1
        lFilenum = int(files[-1])
        return lFilenum+1

    def logoCat():
        path = vars_setup.catPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Catlog-","")
            cnt += 1
        lFilenum = int(files[-1])
        return lFilenum+1

    def ss():
        path = vars_setup.ssPath
        files = os.listdir(path)
        cnt = 0
        while cnt != len(files):
            files[cnt] = files[cnt].replace("Photo-","")
            files[cnt] = files[cnt].replace(".png","")
            cnt += 1
        lFilenum = int(files[-1])
        return lFilenum+1

    numDict = {
        1: pic,
        2: vid,
        3: logo,
        4: logoCat,
        5: ss
    }
    if method in numDict:
        numDict[method]()
