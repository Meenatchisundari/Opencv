#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import cv2


# In[3]:


img1=cv2.imread("C:/Users/ASUS/Downloads/Bird image")
img2=cv2.imread("C:/Users/ASUS/Downloads/Sample.jpg")


# In[4]:


plt.imshow(img1)


# In[5]:


plt.imshow(img2)


# In[6]:


print(img1.shape)
print(img2.shape)


# In[7]:


img3=cv2.resize(img1,(400,200))
img4=cv2.resize(img2,(400,200))


# In[8]:


plt.imshow(img3)


# In[9]:


plt.imshow(img4)


# In[10]:


blended=cv2.addWeighted(img3,1,img4,0.4,0)
plt.imshow(blended)

