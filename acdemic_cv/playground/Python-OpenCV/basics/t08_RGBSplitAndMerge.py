# -*- coding: utf-8 -*-
"""
Python: cv.Split(src, dst0, dst1, dst2, dst3) → None
Parameters:	
src – input multi-channel array.
mv – output array or vector of arrays; in the first variant of the function the number of arrays must match src.channels(); the arrays themselves are reallocated, if needed.
The functions split split a multi-channel array into separate single-channel arrays:

\texttt{mv} [c](I) =  \texttt{src} (I)_c

If you need to extract a single channel or do some other sophisticated channel permutation, use mixChannels() .

See also merge(), mixChannels(), cvtColor()

"""

import cv2.cv as cv

orig = cv.LoadImage('img/blueRose.jpeg')
b = cv.CreateImage(cv.GetSize(orig), orig.depth, 1)
g = cv.CloneImage(b)
r = cv.CloneImage(b)
cv.Split(orig, b, g, r, None)

merged = cv.CreateImage(cv.GetSize(orig), 8, 3)
cv.Merge(g, b, r, None, merged)

cv.ShowImage('Origin', orig)
cv.ShowImage('Blue', b)
cv.ShowImage('Green', g)
cv.ShowImage('Red', r)
cv.ShowImage('Merged', merged)

cv.WaitKey(0)
cv.DestroyAllWindows()