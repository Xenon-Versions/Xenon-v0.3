import os
import cv2
import time
import pyautogui as gui

print("Wait for mirror to get activated")

def destroy():
    wins = gui.getWindowsWithTitle("Xenon Mirror-Backend")
    wins[0].close()

os.system("title Xenon Mirror-Backend")
print("Press q to exit mirror")

try:
    cap = cv2.VideoCapture(0)
    while True:
        # Read video frame by frame
        success, img = cap.read()

        # Flip the image(frame)
        img = cv2.flip(img, 1)

        cv2.imshow("Mirror",img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
except:
    print("No Camera found\n\nClosing this window in 5 seconds")
    time.sleep(5)
    quit()
    destroy()

print("Closing this window in 5 secnods")
quit()
destroy()