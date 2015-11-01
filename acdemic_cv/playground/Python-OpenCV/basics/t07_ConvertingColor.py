import cv2.cv as cv

img = cv.LoadImage('img/blueRose.jpeg', cv.CV_LOAD_IMAGE_COLOR)
rose = cv.CreateImage(cv.GetSize(img), cv.CV_8UC2, 3)
cv.Convert(img, rose)
cv.ShowImage('converting - press key \'space\' to invoke convert', rose)

k = cv.WaitKey(0)
#assert k == 32 # space
rose2 = cv.CreateImage(cv.GetSize(img), cv.CV_8UC2, 3)
cv.CvtColor(img, rose2, cv.CV_RGB2BGR)
cv.ShowImage('CvtColor', rose2)
k = cv.WaitKey(0)
if k == 27:
    cv.DestroyAllWindows()


