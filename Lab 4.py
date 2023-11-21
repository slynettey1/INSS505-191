#step 2
for i in range(11):
    print(i)
#step 3
for i in range(1,11):
    print(i)
#step 4
for i in range(1,11,2):
    print(i)
#step 5
radius = int(input("Enter the radius of a circle:"))
#step 6
import math
pi =math.pi
#step 7
if radius > 0:
    area_circle =pi * (radius**2)
    print("Area of circle", area_circle)
else:
    print("Input parameters are not greater than 0,cannot compute area of polygon requested.")
#step 8
length = int(input("Enter the length of the rectangle: "))
#step 9
width = int(input("Enter the width of the rectangle:"))
#step 10
if length > 0 and width >0:
    area_rectangle = length * width
    print("Area of a rectangle", area_rectangle)
else:
    print("input parameters are not greater than0. can not compute the area of the polygon requested.")
#step 11
if radius > 0:
    area_circle = pi * (radius**2)
    print("Area of a circle",area_circle)
else:
    print("input parameters are not greater than 0. Cannot compute the area of thr polygon requested.")
if length >0 and width > 0:
    area_rectangle = length * width
    print("Area of the rectangle", area_rectangle)
else:
    print("Input parameters are not greater than 0. cannot compute the area of the polygon requested.")

