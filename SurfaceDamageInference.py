
# coding: utf-8

# In[1]:


# from __future__ import print_function, division
import torch
# import torch.nn as nn
# import torch.optim as optim
# from torch.autograd import Variable
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import PIL
from PIL import Image
from PIL import ImageFile
import cv2
import imageio
ImageFile.LOAD_TRUNCATED_IMAGES = True


# In[2]:


model = torch.load("modelnew")
classes = {0:"HighDamage",1:"LowDamage",2:"MediumDamage",3:"NoDamage"}


# In[3]:


def detect(frame,net,transform):
    frame = PIL.Image.fromarray(frame)
    print(frame.size)
    # detections = [batch,number_classes_detected,{score,x0,y0,x1,y1}]
    return frame


# In[4]:


transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


# In[5]:


video_capture = cv2.VideoCapture(1)
video_capture.open(1)
print(video_capture.isOpened())
while True:
    _,frame = video_capture.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     gray = np.array(gray, dtype=np.uint8)
#     canvas = detect(gray,model.eval(),transform)
   
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    img=transform(img)
    img=np.asarray(img)
    img=torch.from_numpy(img)
    
    img=img.view(1,3,224,224)
    
    model.eval()
    y_ = model(img)
    _, y_label_ = torch.max(y_, 1)
    print(classes[y_label_.data.cpu().numpy()[0]])
    
    cv2.imshow("frame", frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

