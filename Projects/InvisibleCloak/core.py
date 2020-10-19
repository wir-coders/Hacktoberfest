import cv2
import numpy as np
import colorpicker
import imutils


color = colorpicker.color()
cap = cv2.VideoCapture(0)

cXprev = 0
cYprev = 0



fourcc = cv2.VideoWriter_fourcc(*'XVID')  #For the saved video codec
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) #For the saved video codec

while(True):
    _, frame = cap.read()
    framecvt = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blue = cv2.inRange(framecvt, color[0], color[1])

    #cv2.imwrite('frame.jpg', frame) #Run this line with only background for the first time, then rerun the code with this line commented out

    bg = cv2.imread('frame.jpg')   # Two Array - Frame, bg

    mask1 = cv2.morphologyEx(blue, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    mask = cv2.bitwise_not(mask1)
    mask1 = cv2.bitwise_and(frame, frame, mask = mask)
    mask2 = cv2.bitwise_and(bg, bg, mask = blue)

    res = mask1 + mask2

    cv2.imshow('hum bhi harry', res)

    out.write(res) #Saving video...


    if cv2.waitKey(1) & 0xFF == ord('q'):
        np.set_printoptions(threshold=np.inf)
        print(mask.shape)
        print(mask1.shape)
        break

cap.release() #Releases Webcam
out.release() #Saves video
cv2.destroyAllWindows()
