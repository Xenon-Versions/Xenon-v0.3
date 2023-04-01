import os
import vars_setup
import pyautogui as gui

def restart(realtimeVars):
    os.system(f"start cmd /K python {vars_setup.xenonPath}")
    user = vars_setup.Personal()
    wins = gui.getWindowsWithTitle(user.title())
    wins[0].close()
    wins = gui.getWindowsWithTitle("Please wait...")
    wins[0].close()