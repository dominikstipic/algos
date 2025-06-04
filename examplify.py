"""
    Given a time, calculate the angle between the hour and minute hands
"""
from math import pi

def to_degree(rad):
    return 360/(2*pi)*rad

def min2degree(min):
    return min*360/60

def calibrate(minutes):
    return (15*min2degree(minutes))/360

def to_angle(xh, xm):
    one_degree = 360/60
    degree_min = one_degree*xm
    xh = 5*xh
    hours_fixed = one_degree*xh
    hours_var = hours_fixed + calibrate(xm)
    return abs(hours_var - degree_min)  



print(to_angle(3, 27))
print(to_angle(3, 5))
print(to_angle(3, 0))