import numpy as np
import cv2
from matplotlib import pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


test_point = [[np.float32(500.0),np.float32(500.0)]]
pt = np.array(test_point)
prev = np.uint8(rgb2gray(plt.imread("prev.jpeg")))
next_image = np.uint8(rgb2gray(plt.imread("next.jpeg")))
Pts = cv2.calcOpticalFlowPyrLK(prevImg=prev, nextImg=next_image,prevPts=pt, nextPts=None,winSize=(15, 15))

print("points coordinate in next frame, if found, error:")
print(Pts)

plt.imshow(prev)
plt.show()
plt.imshow(next_image)
plt.show()