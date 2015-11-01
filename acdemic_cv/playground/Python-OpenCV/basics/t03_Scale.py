import cv2.cv as cv
img = cv.LoadImage('img/messigray.png')
thumb = cv.CreateImage((img.width/2, img.height/2), 8, 3)
cv.Resize(img, thumb)
cv.SaveImage('img/thumb.png', thumb)