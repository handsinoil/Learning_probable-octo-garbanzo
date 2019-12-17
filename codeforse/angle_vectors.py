import decimal
from math import sqrt, acos

with open('angle2.in') as angle2in:
	x1, y1, x2, y2 =[float(i) for i in angle2in.readline().split()]


print(x1, y1, x2, y2 )
def scalar(x1, y1, x2, y2):
	return abs(x1 * x2 + y1 * y2)


def module(x, y):
	return sqrt(x ** 2 + y ** 2)


cos = scalar(x1, y1, x2, y2) / (module(x1, y1) * module(x2, y2))

ang = acos(cos)

with open('angle2.out', mode='wt') as o:
	print('{:.5}'.format(ang), file=o)
