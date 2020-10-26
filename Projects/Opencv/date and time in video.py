import cv2
import datetime
cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))



while cap.isOpened():
    ret ,frame = cap.read()
    if ret ==True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:'+str(cap.get(3)) +'XHeight:'+str(cap.get(4))
        dd = str(datetime.datetime.now())
        frame = cv2.putText(frame,dd,(10,25),font,1,(48,199,48),2,cv2.LINE_AA)
        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):#while you pressing 'q' you can exit from the window 
            break;
    else:
        break;

cap.release()
cv2.destroyAllWindows()

            
