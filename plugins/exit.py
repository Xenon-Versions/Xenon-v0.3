import pyautogui as gui
import vars_setup

def leaveIt():
    user = vars_setup.Personal()
    wins = gui.getWindowsWithTitle(user.title())
    wins[0].close()