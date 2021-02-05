import cv2
import time
from datetime import datetime

cap = cv2.VideoCapture(0)

prev_frame_time = 0
new_frame_time = 0

while True:
	retrieve, frame = cap.read()

	new_frame_time = time.time()
	fps = 1 / (new_frame_time - prev_frame_time)
	prev_frame_time = new_frame_time

	FPS = "FPS : " + str(fps)

	cv2.putText(
	    frame,
	    FPS,
	    (1, 55),
	    cv2.FONT_HERSHEY_SIMPLEX,
	    1,
	    (255, 0, 0),
	    2,
	)

	print("Conslo Log | ", FPS)

	if not retrieve:
		break

	DT = "Timestamp : " + str(datetime.now())

    	cv2.putText(
        	frame,
        	DT,
        	(1, 25),
        	cv2.FONT_HERSHEY_SIMPLEX,
        	1,
        	(0, 255, 0),
        	2,
    	)

    	print("Console Log | ", DT, " | ", FPS)

    	if not retrieve:
        	break


	frame = cv2.flip(frame, -1)
	cv2.imshow('Vid',frame)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
