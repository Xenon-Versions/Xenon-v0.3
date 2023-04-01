import pyFunc
import os
from datetime import datetime as dt
import pyautogui as gui
import webbrowser as web
import time as ttime
import traceback
import vars_setup

try:
    os.system("title Xenon automation")

    user = pyFunc.getTempData()
    userS = user.split(" ")
    time = userS[1]
    number = userS[2]
    message = user.replace(f"send {time} {number}","")

    timeS = time.split(":")
    hour = int(timeS[0])
    min = int(timeS[1])
    if timeS[2] == "pm":
        hour = hour+12

    Chour = dt.now().hour
    Cmin = dt.now().minute

    print(f"Your message will be send at {time},\nKeep PC alive till then")

    run = True
    while run:
        if Chour == hour:
            if Cmin == min:
                run = False
                link = f"https://web.whatsapp.com/send/?phone={number}&text={message}&type=phone_number&app_absent=0"
                web.open(link)
                wins = gui.getWindowsWithTitle("WhatsApp - Google Chrome")
                wins[0].maximize()
                ttime.sleep(15)
                gui.click(1340,700)
            else:
                Chour = dt.now().hour
                Cmin = dt.now().minute
        else:
            Chour = dt.now().hour
            Cmin = dt.now().minute
    win = gui.getWindowsWithTitle("Xenon automation")
    win[0].close()
except:
    print("Wrng syntax please check\nExmaple:- send 12:00:am 1234567890 This is my message")
    file = open(vars_setup.newPath(vars_setup.dataBasePath,"error-report.txt"),"a")
    file.write(f"\nLatest Error occured on {vars_setup.timeNow}:-")
    traceback.print_exc(file=file)
    quit()