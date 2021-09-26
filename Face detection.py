#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2


face_cascade = cv2.CascadeClassifier("C:/Users/ASUS/Downloads/Face-Recognition_HaarCascade at master · priyanshujoshii_Face-Recognition.html")
cap = cv2.VideoCapture(0)

    
while True:
    check,frame = cap.read()
    
    faces = face_cascade.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5);
    
    
    
   
    for x,y,w,z in faces:    
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),4)

        
    
    cv2.imshow('Face Detector',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()

