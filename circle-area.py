import math

def area_circle(radius):
    area = math.pi * pow(radius, 2)
    return  print('Area of circle is:', area)

radius = int(input('Enter radius of circle:'))

area_circle(radius)