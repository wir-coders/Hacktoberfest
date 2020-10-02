import cv2
import sys
from PIL import Image

imagePath = "three_human.jpg"
cascPath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascPath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

print("Found {0} faces!".format(len(faces)))
img_counter = 0
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    print((x,y,x+w,y+w))
    original = Image.open(imagePath)
    width, height = original.size
    croped_img = original.crop((x,y,x+w,y+w))
    croped_img.save(str(img_counter) + ".jpeg")
    img_counter += 1


#paste faces
new_img = Image.open(imagePath)
im2 = Image.open("0.jpeg")
new_img.paste(im2,(133, 71))
new_img.show()

