import numpy

#  more efficient to do interations than pandas
#  Pandas and OpenCV is BASED ON NUMPY

m = numpy.array([[123, 12, 123, 12, 33], [0], []])
l = numpy.asarray([[123, 12, 123, 12, 33], [0], []])

n = numpy.arange(27)
type(n)

n.reshape(3, 9)
n.reshape(3, 3, 3)
