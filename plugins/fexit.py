import pyautogui as gui
def fexit():
    wins = gui.getActiveWindow()
    wins.minimize()
