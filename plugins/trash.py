import time

import vars_setup
import os
import pyautogui as gui
import funcs
import cv2

def startMsg():
    os.system("cls")
    try:
        print(vars_setup.Messages.startMsg(True))
    except:
        print(vars_setup.Messages.startMsgNW(True))

def desk():
    funcs.printAndSay("Redirecting to Desktop")
    gui.hotkey("win","d")

def mirror(user):
    funcs.printAndSay("Please wait")
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'mirror.py')}")

def vidCap():
    funcs.printAndSay("Please wait")
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'vidCap.py')}")

def photoCap():
    filenum = funcs.getNum(1)
    camera = cv2.VideoCapture(0)
    funcs.printAndSay("Taking photo in 10 seconds")
    rate,img = camera.read()
    cv2.imwrite(vars_setup.newPath(vars_setup.picPath,f"Photo{filenum}.jpg"),img)
    funcs.printAndSay("Photo taken")
    os.startfile(vars_setup.newPath(vars_setup.picPath,f"Photo{filenum}.jpg"))