#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pylab as plt
import cv2
import numpy as np


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

def process(image):
    
    if image.any() !=None:
        
        height = image.shape[0]
        width = image.shape[1]
        region_of_interest_vertices = [
            (0,height),
            (width/2,height/2 + 40),
            (width, height)
        ]
        gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        canny_image = cv2.Canny(gray_image, 120, 120)
        cropped_image = region_of_interest(canny_image,
                        np.array([region_of_interest_vertices], np.int32),)
        
        
        hough_transform(cropped_image)
       
    
    
    
    return cropped_image


def hough_transform(image):
    lines = cv2.HoughLinesP(image,
                            rho=2,
                            theta=np.pi/180,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    
    
    print(lines)

cap = cv2.VideoCapture("C:/Users/ASUS/Downloads/solidWhiteRight.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    frame = process(frame)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(60) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




