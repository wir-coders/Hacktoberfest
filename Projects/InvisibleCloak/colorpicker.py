import cv2
import numpy as np

def color():
    cap = cv2.VideoCapture(1)

    while True:
        _, frame = cap.read()
        roi = frame[100:300, 0:200]
        roicvt = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

        minn = np.min(roicvt, axis = 1)
        actualmin = np.min(minn, axis = 0)
        maxx = np.max(roicvt, axis = 1)
        actualmax = np.max(maxx, axis = 0)

        cv2.imshow('Only view colored object in this frame', roicvt)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            return[actualmin, actualmax]

    cap.release()
    cv2.destroyAllWindows()