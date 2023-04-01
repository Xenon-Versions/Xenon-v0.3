import webbrowser as web
import pyautogui as gui
import os
import pyFunc

os.system("title Server")

wins = gui.getWindowsWithTitle("Server")
wins[0].minimize()

web.open("http://localhost:1234")
wins = gui.getWindowsWithTitle("Google Chrome")
wins[0].maximize()

os.system("python -m http.server 1234")

"""path = os.getcwd()
try:
    indexPath = vars_setup.newPath(path,"index.html")
    file = open(indexPath,"r")
    funcs.printAndSay("Index file found")
except:
    funcs.printAndSay("Index file not found")
"""