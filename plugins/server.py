import os
import funcs
import vars_setup
import pyautogui as gui

def launch(user):
    funcs.printAndSay("This server is only for this device\nVisit - http://localhost:1234 title Server")
    os.system(f"start cmd /K python {vars_setup.newPath(vars_setup.dataBasePath,'server.py')}")

empty_list = []

def close():
    try:
        wins = gui.getWindowsWithTitle("Server")
        wins[0].close()
        funcs.printAndSay("Server closed")
    except:
        funcs.printAndSay("No active server found")