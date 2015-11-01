import cv2.cv as cv

orig = cv.LoadImage('img/blueRose.jpeg')
b = cv.CreateImage(cv.GetSize(orig), orig.depth, 1)
g = cv.CloneImage(b)
r = cv.CloneImage(b)
cv.Split(orig, b, g, r, None)

#merged = cv.CreateImage(cv.GetSize(orig), 8, 3)
#cv.Merge(g, b, r, None, merged)

cv.ShowImage('Origin', orig)
cv.ShowImage('Blue', b)
cv.ShowImage('Green', g)
cv.ShowImage('Red', r)
#cv.ShowImage('Merged', merged)
rcp = cv.CloneImage(r)

cv.WaitKey(0)
cv.DestroyAllWindows()