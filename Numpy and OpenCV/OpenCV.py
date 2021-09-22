import cv2
import numpy

im_g = cv2.imread("smallgray.png", 0)
cv2.imwrite("newsmallgray.png", im_g)

a = im_g[0:2]
type(im_g)

for i in im_g.T:
    print(i)

ims = numpy.hstack((im_g, im_g, im_g))

lst = numpy.hsplit(ims, 3)
