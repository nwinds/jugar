import cv2
import numpy as np

image = cv2.imread("img/cat.jpg") #Load image

imageWidth = image.shape[1] #Get image width
imageHeight = image.shape[0] #Get image height

xPos, yPos = 0, 0

while xPos < imageWidth: #Loop through rows
    while yPos < imageHeight: #Loop through collumns

        image.itemset((yPos, xPos, 0), 255) #Set B to 255
        image.itemset((yPos, xPos, 1), 255) #Set G to 255
        image.itemset((yPos, xPos, 2), 255) #Set R to 255

        yPos = yPos + 1 #Increment Y position by 1

    yPos = 0
    xPos = xPos + 1 #Increment X position by 1

cv2.imwrite("img/result.bmp", image) #Write image to file