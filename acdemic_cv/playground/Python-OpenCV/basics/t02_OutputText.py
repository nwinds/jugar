import cv2.cv as cv
#read img
img = cv.LoadImage('img/image.png', cv.CV_LOAD_IMAGE_COLOR)
font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 3, 8)

x = img.height / 2
y = img.width / 4

cv.NamedWindow('a_window', cv.CV_WINDOW_AUTOSIZE)
cv.PutText(img, 'Hello World!', (x, y), font, cv.RGB(255, 255, 255))
cv.ShowImage('Hello World', img)

k = cv.WaitKey(0)
if k == 27:
    cv.DestroyAllWindows()
