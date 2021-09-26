#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
img=np.zeros((512,512,3),np.int8)


# In[ ]:


def just_print_for_all(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(0,0,255),-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img, pt1=(x,y), pt2=(x+100,y+100),color=(0,255,255),thickness=-1)
cv2.namedWindow(winname= "Image_drawing")
cv2.setMouseCallback("Image_drawing", just_print_for_all)
while True:
    cv2.imshow("Image_drawing", img)
    if cv2.waitKey(10) == 27:
        break
cv2.destroyAllWindows()


# In[ ]:




