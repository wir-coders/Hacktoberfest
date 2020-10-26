import cv2
import numpy as np
#There are different type of mouse events in opencv like left click,right click etc..
# events =[i for i in dir(cv2) if "EVENT" in i]
# print(events) 

  #callback function

def click_event(event,x,y, flags,param):
    if event ==cv2.EVENT_LBUTTONUP:#Left click on the window display the coordinate of that point in the window.
        print(x,' ',y)
        font = cv2.FONT_HERSHEY_COMPLEX
        string ='('+str(x)+','+str(y)+')'
        cv2.putText(img,string,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('image',img)
    elif event == cv2.EVENT_RBUTTONDOWN:#right click on the window display the colour in the point in (b,g,r) format
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        font = cv2.FONT_HERSHEY_COMPLEX
        colo =str(blue)+','+str(green)+','+str(red)
        cv2.putText(img,colo,(x,y),font,0.5,(255,255,0),1)
        cv2.imshow('image',img)
    
img = cv2.imread("Image.jpeg")
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)#setMouseCallback("window_name",Callbackfunction)


cv2.waitKey(0)
cv2.destroyAllWindows()
