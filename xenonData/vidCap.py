import cv2
import os
import vars_setup
import funcs

print("Wait for camera to get activated")

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
filenum = funcs.getNum(2)
out = cv2.VideoWriter(f'{vars_setup.newPath(vars_setup.vidPath,f"Video-{filenum}.avi")}', fourcc, 20.0, (640, 480))

os.system("title Xenon Video-Capture-Backend")
print("Press q to stop recording")

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('Xenon video capture', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
os.startfile(vars_setup.vidPath)
