import cv2
import numpy as np
from PIL import Image

im = Image.open('mss/100009_1_20210310000723.mp4.jpg') # Image load
im_array = np.asarray(im) # Image to np.array

kernel1d = cv2.getGaussianKernel(5, 3)
kernel2d = np.outer(kernel1d, kernel1d.transpose())

low_im_array = cv2.filter2D(im_array, -1, kernel2d) # convolve

low_im = Image.fromarray(low_im_array) # np.array to Image
low_im.save('gaussian.BMP','BMP')


