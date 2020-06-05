from imutils.video import VideoStream
import imutils
import time
import cv2 
import numpy as np
 # initialize the video stream and allow the cammera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
panel=np.zeros([100,700],np.uint8)
cv2.namedWindow("panel")
def nothing(x):
    pass
cv2.createTrackbar("L-h","panel",0,255,nothing)
cv2.createTrackbar("U-h","panel",255,255,nothing)

cv2.createTrackbar("L-s","panel",0,179,nothing)
cv2.createTrackbar("U-s","panel",179,179,nothing)

cv2.createTrackbar("L-v","panel",0,255,nothing)
cv2.createTrackbar("U-v","panel",255,255,nothing)

while True:
    frame= vs.read()
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    lower_green=np.array([0,0,0])
    upper_green=np.array([255,70,255])
    
    
    mask = cv2.inRange(hsv,lower_green,upper_green)
    cv2.imshow("Frame",frame)
    cv2.imshow("mask", mask)
    cv2.imshow("panel",panel)
    key=cv2.waitKey(30) & 0xFF
    if key==ord("q"):
        break
cv2.destroyAllWindows()