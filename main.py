import cv2
import numpy as np

foreground=cv2.imread('giraffe.jpeg')
background=cv2.imread('safari.jpeg')

#print(foreground)
width=foreground.shape[1]
height=foreground.shape[0]

# Resize the background image to match the size of the foreground
background=cv2.resize(background, (width, height))

for x in range(width):
  for y in range(height):
    pixel=foreground[y,x]
    #print type(pixel)
    if np.any(pixel==[2,255,6]):
      foreground[y,x]=background[y,x]

cv2.imwrite('output.jpeg', foreground)
  