# -*- coding: utf-8 -*-
from element import *
import cv2
import numpy as np

#import cv2.cv as cv
# code from http://segmentfault.com/a/1190000003742433
# as a demo to make a comparation with self-impl ver.
def demoOpenCV():
    image=cv.LoadImage('img/cat.jpg', cv.CV_LOAD_IMAGE_COLOR) #Load the image
    cv.ShowImage('Original', image)

    grey = cv.CreateImage((image.width ,image.height),8,1) #8depth, 1 channel so grayscale
    cv.CvtColor(image, grey, cv.CV_RGBA2GRAY) #Convert to gray so act as a filter
    cv.ShowImage('Greyed', grey)

    element_shape = cv.CV_SHAPE_RECT
    pos=3

    element = cv.CreateStructuringElementEx(pos*2+1, pos*2+1, pos, pos, element_shape)
    #print(element)
    cv.Dilate(grey,grey,element,2) #Replace a pixel value with the maximum value of neighboors
    #Note: The Structuring element is optionnal
    cv.ShowImage('OpenCV Dilated', grey)

    cv.WaitKey(0)
    cv.DestroyAllWindows()




def dilateImpl(srcImg, dstImg, element = None, iterations = 1):
    # type checking
    if type(srcImg) != np.ndarray or type(dstImg) != np.ndarray:
        raise Exception('input image type error!')
    if type(iterations) != int or iterations <= 0:
        raise Exception('invalid iterations')
    
    #fake ed: using cv to test function abstraction okay
    #ele = cv.CreateStructuringElementEx(element.colsNum, element.rowsNum, \
    #element.anchorX, element.anchorY, cv.CV_SHAPE_RECT)
#
#    imageWidth = srcImg.shape[1]
#    imageHeight = srcImg.shape[0]
#    xPos, yPos = 0, 0
#
#    while xPos < imageWidth: #Loop through rows
#        while yPos < imageHeight: #Loop through collumns
#
#            srcImg.itemset((yPos, xPos, 0), 255) #Set B to 255
#            srcImg.itemset((yPos, xPos, 1), 255) #Set G to 255
#            srcImg.itemset((yPos, xPos, 2), 255) #Set R to 255
#
#            yPos += 1 #Increment Y position by 1
#
#        yPos = 0
#        xPos = xPos + 1 #Increment X position by 1


        
    #cv.Dilate(srcImg, dstImg, ele, iterations)
    

# interface for dilate operation
def dilateWrapper(greyImg):
    try: 
        print('dilateInter: L61')
        pos=3
        ele = element(pos*2+1, pos*2+1, pos, pos)

        
        dilateImpl(greyImg, greyImg, ele, 2)
        

        cv2.imshow('Dilated image', greyImg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    finally:
        print('dilate over.')
    #except Exception, e:
        #print(str(e))



#demoOpenCV()


# self impl
image=cv2.imread('img/cat.jpg') #Load the image
cv2.imshow('Original', image)
grey = cv2.imread('img/cat.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
#cv.CvtColor(image, grey, cv.CV_RGBA2GRAY) #Convert to gray so act as a filter
cv2.imshow('Greyed', grey)
dilateWrapper(grey)
