from datetime import datetime as dt
import pyFunc
import pyautogui as gui
import os

try:
    os.system("title Xenon Reminder")
    user = pyFunc.getTempData()
    userS = user.split(" ")
    time = userS[1]
    message = user.replace(f"reminder {time}","")
    if message == "":
        message = "No reminding message provided"
    timeS = time.split(":")
    hour = int(timeS[0])
    min = int(timeS[1])
    if timeS[2] == "pm":
        hour = hour+12
    print(f"You will be reminded at {time},\nKeep PC alive till then")
    Chour = dt.now().hour
    Cmin = dt.now().minute
    run = True
    while run:
        if Chour == hour:
            if Cmin == min:
                run = False
                gui.hotkey("win","d")
                pyFunc.alert(title="Reminder",message=f"It's {time}\nSubject: {message}")
            else:
                Chour = dt.now().hour
                Cmin = dt.now().minute
        else:
            Chour = dt.now().hour
            Cmin = dt.now().minute
    win = gui.getWindowsWithTitle("Xenon Reminder")
    win[0].close()
    wins = gui.getWindowsWithTitle("Reminder")
    wins[0].restore()
    wins[0].activate()

except:
    pass
