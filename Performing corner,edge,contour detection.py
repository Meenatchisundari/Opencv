#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
  
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/TASK/Chessboard.jpg") 

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

corners = cv2.goodFeaturesToTrack(gray_img, 100, 0.01, 10) 

corners = np.int0(corners) 

for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, 255, -1) 

cv2.imshow('Corner', img)  
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


import cv2
image = cv2.imread("C:/Users/ASUS/OneDrive/Documents/TASK/Chessboard.jpg")
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
cv2.waitKey(0)
cv2.destroyAllWindows()

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
image_copy = image.copy()
cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow('Contour',image_copy)
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:


import cv2
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/TASK/Chessboard.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) 
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:


mport cv2 as cv  
import numpy as np
img = cv2.imread("C:/Users/ASUS/OneDrive/Documents/TASK/Chessboard.jpg")

def draw_grid(img, grid_shape, color=(0, 255, 0), thickness=1):
    h, w, _ = img.shape
    rows, cols = grid_shape
    dy, dx = h / rows, w / cols

    
    for x in np.linspace(start=dx, stop=w-dx, num=cols-1):
        x = int(round(x))
        cv.line(img, (x, 0), (x, h), color=color, thickness=thickness)

    
    for y in np.linspace(start=dy, stop=h-dy, num=rows-1):
        y = int(round(y))
        cv.line(img, (0, y), (w, y), color=color, thickness=thickness)

    return img
cv2.imshow('Grid',img)
cv2.waitKey(0)

cv2.destroyAllWindows()


# In[ ]:




