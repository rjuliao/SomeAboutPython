import cv2
import numpy

img = cv2.imread('child.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r,c = img.shape
print("Mesaure: ")
a = 2


for i in range(0,r,a):
    for j in range(0,c,a):
        s = img[i,j]+img[i,j+1]+img[i+1,j]+img[i+1,j+1]
        avg = s/4
        img[i,j] = avg
        img[i,j+1] = avg
        img[i+1,j] = avg
        img[i+1,j+1] = avg
        
        
cv2.imshow("Holi", img)
cv2.waitKey()
cv2.destroyAllWindows()

