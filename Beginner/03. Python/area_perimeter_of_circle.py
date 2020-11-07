#program to find area of circle in Python using math file
import math
r = float(input("Enter the radius of the circle: "))
area = math.pi* r * r
peri = 2 * math.pi* r
print("area - %.2f perimeter - %.2f" %(area,peri))