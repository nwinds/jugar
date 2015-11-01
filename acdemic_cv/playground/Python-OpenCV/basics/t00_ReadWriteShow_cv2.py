import numpy as np
import cv2

img = cv2.imread('img/th.jpeg', 0)
cv2.imshow('image', img)

grayImg = cv2.imread('img/th.jpeg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('MyPicGray.png', grayImg)

k = cv2.waitKey(0)
if k == 27: # ESC to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('img/messigray.png', img)
    cv2.destroyAllWindows()