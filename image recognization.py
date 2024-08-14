import cv2
img=cv2.imread("images.jpg")

#h,w=face.shape[:2]
h= int(input("Enter height:"))
w= int(input("Enter width"))

resize =cv2.resize(img,(h,w))
cv2.imshow("out",resize)

face1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("bw.jpg",face1)

cv2.waitKey(0)