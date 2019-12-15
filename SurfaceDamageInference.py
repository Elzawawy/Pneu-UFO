import torch
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import PIL
from PIL import Image
from PIL import ImageFile
import cv2
import imageio
ImageFile.LOAD_TRUNCATED_IMAGES = True

# Inference environment params.
model = torch.load("SurfaceDamageDetectionModel")
classes = {0:"HighDamage",1:"LowDamage",2:"MediumDamage",3:"NoDamage"}

def detect(frame,net,transform):
    frame = PIL.Image.fromarray(frame)
    print(frame.size)
    return frame
# define pro-processing applied to images in a transformation object.
transform = transforms.Compose([
        transforms.Resize(224),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

video_capture = cv2.VideoCapture(1)
video_capture.open(1)
print(video_capture.isOpened())
while True:
    _,frame = video_capture.read()
   # pre-process the frame entered from camera feed.
    img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    img=Image.fromarray(img)
    img=transform(img)
    img=np.asarray(img)
    img=torch.from_numpy(img)
    img=img.view(1,3,224,224)
    # pass the image produced to the model and print the output of the predicted label.
    model.eval()
    y_ = model(img)
    _, y_label_ = torch.max(y_, 1)
    print(classes[y_label_.data.cpu().numpy()[0]])
    cv2.imshow("frame", frame)
    # provide a way for exit from the main loop program.
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

