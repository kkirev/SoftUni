"""
Create a function that calculates and returns the area of a rectangle by given width and height.
Print the result on the console.
"""


def trangle_area(a, b):
	area = a * b
	return area


width = float(input())
height = float(input())

area = trangle_area(width, height)
print(int(area))