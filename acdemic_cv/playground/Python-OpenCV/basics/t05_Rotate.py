import cv2
import numpy as np

img = cv2.imread('img/th.jpeg', 0)
rows, cols = img.shape

matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, matrix, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()