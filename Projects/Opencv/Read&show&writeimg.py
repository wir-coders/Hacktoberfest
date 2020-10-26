import cv2;

img =cv2.imread('Image.jpeg',0)


cv2.imshow('image',img)
k=cv2.waitKey(0)
if(k==27):#unicode correspoding to else:27
    cv2.destroyAllWindows()
elif k==ord('s'):#ord() this function will accepts string of length 1 and returns unicode corresponding value
    cv2.imwrite('Sample.jpg',img)#on pressing 's' it will save the image.jpeg as sample.jpeg in gray scale format
    cv2.destroyAllWindows()
cv2.waitKey(1)
