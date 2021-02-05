import cv2
import numpy as np

vid = cv2.VideoCapture(0)

while(True):

    ret, frame = vid.read()
    img=cv2.flip(frame, -1)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()

