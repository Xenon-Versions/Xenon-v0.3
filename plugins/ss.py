import time
import funcs
import pyautogui as gui
import vars_setup


"""
import pyautogui as gui
import time


wins = gui.getWindowsWithTitle("J.V.K")
wins[0].restore()


time.sleep(1)


w = wins[0].width
h = wins[0].height
l = wins[0].left
t = wins[0].top

ss = gui.screenshot(imageFilename="ssFile.png",region=(l,t,w,h))
"""

def winSS(appName,filenum):
    wins = gui.getWindowsWithTitle(appName)
    wins[0].restore()
    wins[0].activate()
    time.sleep(1)
    w = wins[0].width
    h = wins[0].height
    l = wins[0].left
    t = wins[0].top
    gui.screenshot(imageFilename=vars_setup.newPath(vars_setup.ssPath,f"ScreenShot-{filenum}.png"), region=(l, t, w, h))

def ssHandeler(user):
    try:
        appName = user[3:]
        filenum = funcs.getNum(5)
        winSS(appName,filenum)
    except:
        filenum = funcs.getNum(5)
        gui.screenshot(imageFilename=vars_setup.newPath(vars_setup.ssPath,f"ScreenShot-{filenum}.png"))
