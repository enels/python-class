from math import pi


def multiply_by_two(number):
    res = number * 2
    return res

def rectangle_perimeter (len1, len2):
    '''
    function to find the perimeter of a rectangle
    :param len1: length
    :param len2: breath
    :return: area of rectangle(float or int)
    '''

    return len1 * len2

def csa_cylinder(r, h):
    '''
    find the curved surface area of a cylinder
    :param r: radius
    :param h: height
    :return: float or int
    '''

    return 2 * pi * r * h

def final_amt()