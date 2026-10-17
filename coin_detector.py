import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread("coin.jpg")

crop=img[50:600,320:840]
img_copy=crop.copy()
img_blur=cv2.GaussianBlur(crop,(5,5),3)
img_gray=cv2.cvtColor(img_blur,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(img_gray,227,255,cv2.THRESH_BINARY)
contours, hierarchy =cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

area=[]
for i in range(len(contours)):
    cnt=contours[i]
    ar=cv2.contourArea(cnt)
    area.append(ar)
print(area)

sorted_indices = np.argsort(area)[::-1]


num = np.sum(np.array(area)[sorted_indices] > 500)

for i in range(1,num):
    cv2.drawContours(img_copy, contours, int(sorted_indices[i]), (0, 255, 0), 3)

cv2.putText(img_copy, f"Number of Coins: {num-1}", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2 )
cv2.imshow("Coin",img_copy)
cv2.imwrite("output.jpg",img_copy)
cv2.waitKey(0)
cv2.destroyAllWindows()
