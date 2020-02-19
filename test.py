
# import the necessary packages
import numpy as np
import cv2
import os
import glob
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Read image
image = cv2.imread(os.path.join("images","rha_keyboard_on2.PNG"))

def applyThresh(image, threshold):
    """
    Apply threshold to binary image. Setting to '1' pixels> minThresh & pixels <= maxThresh.
    """
    binary = np.zeros_like(image)
    binary[(image > threshold[0]) & (image <= threshold[1])] = 1
    return binary

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = (10, 75)
bin_gray = applyThresh(gray, thresh)
print(np.unique(bin_gray))
print(255*bin_gray)

# # Display
# f, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 9))  # width and heights in inches
# f.tight_layout()
# ax1.imshow(gray, cmap='gray')
# ax1.set_title('Gray Image', fontsize=50)
# ax2.imshow(bin_gray, cmap="gray")
# ax2.set_title('Binary Gray Image', fontsize=50)
# plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)

# R = image[:,:,0]
# G = image[:,:,1]
# B = image[:,:,2]

# thresh = (150, 255)
# thresh = (20, 150)
# bin_R = applyThresh(R, thresh)
# bin_G = applyThresh(G, thresh)
# bin_B = applyThresh(B, thresh)

bin_GG = np.dstack((255*bin_gray,255*bin_gray,255*bin_gray))
cv2.imshow("win", bin_GG)
cv2.waitKey(0)
cv2.destroyAllWindows

cv2.imwrite("rha_keyboard_off3.PNG", bin_GG)

