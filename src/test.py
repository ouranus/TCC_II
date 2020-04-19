import cv2
#importing numpy
import numpy as np
image=cv2.imread('2.jpg')
cv2.imshow('hello_world', image)
#shape function is very much useful when we are looking at a dimensions of an array, it returns a tuple which gives a dimension of an image
print(image.shape)
cv2.waitKey()
cv2.destroyAllWindows()
