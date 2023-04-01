import os

import time
import pyautogui as gui
import pyFunc

os.system("title Xenon Timer")

num = int(pyFunc.getTempData())
cnt = 0
while cnt != num:
    cnt += 1
    os.system("cls")
    print(f"Time left: {num-cnt}")
    time.sleep(1)
title = "Times Up!"
if num == 1:
    message = "Your [1] second is over"
else:
    message = f"Your [{num}] seconds are over"

gui.hotkey("win","d")
pyFunc.alert(title=title,message=message)
wins = gui.getWindowsWithTitle("Xenon Timer")
wins[0].close()