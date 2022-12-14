# -*- coding: utf-8 -*-
"""Assign 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L6ZMV6Xs4dY1EGDj0JPILpx6i9TwpmVm

# **Photo 1**
"""

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))

"""# **Photo 2** """

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo1.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))

"""# **Photo 3**"""

from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo2.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))

"""# **Blurring**"""

import cv2
# from PIL import Image
import matplotlib.pyplot as plt

# Open image using openCV2
img = cv2.imread("photo.jpg")
  
# Notice the COLOR_BGR2RGB which means that the color is
# converted from BGR to RGB
color_coverted = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  
# using pillow
# pil_image = Image.fromarray(color_coverted)
# pil_image.show()

# using matplotlib
# plt.figure(figsize=(10,10))
plt.imshow(color_coverted)
plt.show()

def displayImage(image):
    if len(image.shape)==3:
        color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(color_coverted)
        plt.show()
        
    else:
        plt.imshow(image, cmap="gray")
        plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = np.zeros((512,512,3), np.uint8)

displayImage(img)

# how to change to color
# img[:] = 255,0,0

# color some parts
# img[200:300,100:300] = 255,0,0

# draw a line
cv2.line(img,(0,0),(300,300),(0,255,0),3)

# img.shape[1] is width, img.shape[0] is heigth
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

#draw rectangle
cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

#draw rectangle (filled)
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

# draw circle
cv2.circle(img, (400,50),30,(255,255,0),5)

# parameters: image,what is the text,start point,font, scale,color, thickness
cv2.putText(img,"OPENCV",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0), 3)


displayImage(img)

kernel = np.ones((3,3), np.float32)/9 # box filter

"""**Photo**"""

img = cv2.imread("photo.jpg")
grayImage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage, -1,kernel)

# pil_img = Image.fromarray(convolvedImg)
# pil_img.show()

displayImage(convolvedImg)

imgBlur = cv2.GaussianBlur(grayImage,(7,7),5)
# median = cv2.medianBlur(img,5)
# blur = cv2.bilateralFilter(img,9,75,75)

# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()

displayImage(imgBlur)

"""# **Canning and Sobel Detection**

**Photo**
"""

# canny
imgCanny = cv2.Canny(imgBlur,20,70)

# sobel
sobelx = cv2.Sobel(imgBlur, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur, cv2.CV_8U,0,1,ksize=3)
imgSobel = sobelx + sobely

# Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,-1]])
img_prewittx = cv2.filter2D(imgBlur,-1,kernelx)
img_prewitty = cv2.filter2D(imgBlur,-1,kernely)
imgPrewitt = img_prewittx + img_prewitty

# # Displaying the converted image
# pil_img = Image.fromarray(imgCanny)
# pil_img.show()

# pil_img = Image.fromarray(imgSobel)
# pil_img.show()

# pil_img = Image.fromarray(imgPrewitt)
# pil_img.show()

displayImage(imgCanny)
displayImage(imgSobel)
displayImage(imgPrewitt)

"""**Photo 1**"""

img = cv2.imread("photo1.jpg")
grayImage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage, -1,kernel)

# pil_img = Image.fromarray(convolvedImg)
# pil_img.show()

displayImage(convolvedImg)

imgBlur = cv2.GaussianBlur(grayImage,(7,7),5)
# median = cv2.medianBlur(img,5)
# blur = cv2.bilateralFilter(img,9,75,75)

# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()

displayImage(imgBlur)

# canny
imgCanny = cv2.Canny(imgBlur,20,70)

# sobel
sobelx = cv2.Sobel(imgBlur, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur, cv2.CV_8U,0,1,ksize=3)
imgSobel = sobelx + sobely

# Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,-1]])
img_prewittx = cv2.filter2D(imgBlur,-1,kernelx)
img_prewitty = cv2.filter2D(imgBlur,-1,kernely)
imgPrewitt = img_prewittx + img_prewitty

# # Displaying the converted image
# pil_img = Image.fromarray(imgCanny)
# pil_img.show()

# pil_img = Image.fromarray(imgSobel)
# pil_img.show()

# pil_img = Image.fromarray(imgPrewitt)
# pil_img.show()

displayImage(imgCanny)
displayImage(imgSobel)
displayImage(imgPrewitt)

"""**Photo 2**"""

img = cv2.imread("photo2.jpg")
grayImage = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
convolvedImg = cv2.filter2D(grayImage, -1,kernel)

# pil_img = Image.fromarray(convolvedImg)
# pil_img.show()

displayImage(convolvedImg)

imgBlur = cv2.GaussianBlur(grayImage,(7,7),5)
# median = cv2.medianBlur(img,5)
# blur = cv2.bilateralFilter(img,9,75,75)

# Displaying the converted image
# pil_img = Image.fromarray(imgBlur)
# pil_img.show()

displayImage(imgBlur)

# canny
imgCanny = cv2.Canny(imgBlur,20,70)

# sobel
sobelx = cv2.Sobel(imgBlur, cv2.CV_8U,1,0,ksize=3)
sobely = cv2.Sobel(imgBlur, cv2.CV_8U,0,1,ksize=3)
imgSobel = sobelx + sobely

# Prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,-1]])
img_prewittx = cv2.filter2D(imgBlur,-1,kernelx)
img_prewitty = cv2.filter2D(imgBlur,-1,kernely)
imgPrewitt = img_prewittx + img_prewitty

# # Displaying the converted image
# pil_img = Image.fromarray(imgCanny)
# pil_img.show()

# pil_img = Image.fromarray(imgSobel)
# pil_img.show()

# pil_img = Image.fromarray(imgPrewitt)
# pil_img.show()

displayImage(imgCanny)
displayImage(imgSobel)
displayImage(imgPrewitt)