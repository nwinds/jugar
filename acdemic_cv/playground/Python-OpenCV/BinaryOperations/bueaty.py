# -*- coding: utf-8 -*-
import cv2.cv as cv

import random

# 这里也可以使用 Get2D/Set2D 来加载图片
im = cv.LoadImage("../basics/img/cat.jpg") 

for k in range(5000): #Create 5000 noisy pixels
    i = random.randint(0,im.height-1)
    j = random.randint(0,im.width-1)
    color = (random.randrange(256),random.randrange(256),random.randrange(256))
    im[i,j] = color

cv.ShowImage("Noize", im)
cv.WaitKey(0)
cv.DestroyAllWindows()