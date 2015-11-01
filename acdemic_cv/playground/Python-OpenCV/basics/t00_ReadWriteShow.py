import cv2.cv as cv
#read img
img = cv.LoadImage('img/image.png', cv.CV_LOAD_IMAGE_COLOR)
#OR
#img = cv.LoadImage('img/image.png')

#show img
cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('a_window', img)

#write img
thumb = img
cv.SaveImage('img/thumb.png', thumb)
cv.WaitKey(0)