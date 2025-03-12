# Given a time, calculate the angle between the hour and minute hands
from math import pi

hour = 12
minute = 15

def from_rad(rad):
    return rad/(2*pi)*360

def from_degree(degree):
    return degree/(360)*2*"PI"


x = from_rad(70)
print(x)