import cv2 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

#cap.isOpened()=>will return true value if cammera is linked or file name is correct and false in other case
while cap.isOpened():
    ret,frame=cap.read()#ret will store true or false if frame store image the it store true else false , frame will store instant capture frames
    if ret:   
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) used to change the colout of image
        #cv2.imshow('frame',frame)
        out.write(frame)
        cv2.imshow('video',frame)
        
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break 
    else:
        break       
cap.release()
out.release() 
cv2.destroyAllWindows() 
