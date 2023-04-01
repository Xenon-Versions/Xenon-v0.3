import pyautogui as gui
import funcs

def max(user):
    winS = user[4:]
    wins = gui.getWindowsWithTitle(winS)
    wins[0].maximize()
    funcs.printAndSay(f" Minimixed {wins[0].title}")


def mini(user):
    winS = user[5:]
    wins = gui.getWindowsWithTitle(winS)
    wins[0].minimize()
    funcs.printAndSay(f"Minimixed {wins[0].title}")

def show(user):
    winName = user[5:]
    wins = gui.getWindowsWithTitle(winName)
    wins[0].restore()
    wins[0].activate()
    funcs.printAndSay(f"Showing {wins[0].title}")

def closeWin(user):
    winName = user[4:]
    wins = gui.getWindowsWithTitle(winName)
    wins[0].restore()
    wins[0].activate()
    funcs.printAndSay(f"Closed {wins[0].title}")

def winHandler(user):
    userS = user.split(" ")
    command = userS[0]
    if command == "max":
        max(user)
    if command == "mini":
        mini(user)
    if command == "cls":
        closeWin(user)
    if command == "show":
        show(user)