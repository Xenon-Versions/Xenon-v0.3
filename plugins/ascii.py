import art
import vars_setup
import os
import pyautogui as gui

def listArt():
    cnt = 0
    fonts = art.ASCII_FONTS
    while cnt != len(fonts):
        print(f"[{cnt}]: {fonts[cnt]}")
        cnt += 1

def catlog():
    cnt = 0
    fonts = art.ASCII_FONTS
    while cnt != len(fonts):
        print(f"[{cnt}]: {fonts[cnt]}")
        art.tprint("TEST",font=fonts[cnt])
        cnt += 1

def asciiHandler(user):
    userS = user.split(" ")
    if len(userS) >= 3:
        if userS[0] == "art":
            try:
                userS[1] = int(userS[1])
                num = int(userS[1])
                text = user.replace(f"art {num}","")
                art.tprint(text,art.ASCII_FONTS[num])
            except:
                font = userS[1]
                text = user.replace(f"art {font}","")
                art.tprint(text,font)
    else:
        text = user.replace("art","")
        art.tprint(text)
    if userS[1] == "list":
        listArt()
    if userS[1] == "catlog":
        catlog()
