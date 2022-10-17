#!/usr/bin/env python3
# It will help reader,informing that code is in python3.
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
__author__ = "JAY DAVE"
__contact__ = "jdave1@stevens.edu"
__date__ = "2022/09/18"
__license__ = "XYZ"
__maintainer__ = "JAY DAVE"
__version__ = "1.0.0"
# ---------------------------------------------------------------------------

"""
AIM of SCRIPT:
The objective of this assignment is for you to (a) develop a set of tests for an
existing triangle classification program, (b) use those tests to find and fix
defects in that program, and (c) report on your testing results for the Triangle problem

"""

def classify_triangle(a,b,c):
    """
    This function returns a string with the type of triangle from three  values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if a == 0 or b == 0 or c == 0:
        return 'InvalidInputTriangle'

    if (a + b > c) and (b + c > a) and (c + a > b):
    #   If two sides summation is greater than third side, then it's a triangle.
        if ((a*a + b*b) == c*c) or ((b*b + c*c) == a*a) or ((c*c + a*a) == b*b):
            # for right angle triangle, it must satify side_1*side_1 + side_2*side_2 = side_3*side_3
            return 'Right'

        if a == b and b == c:
            # for  Equilateral triangle, it must satify side_1 = side_2 = side_3.
            return 'Equilateral'

        if (a == b and b != c) or (a == c and a != b) or (b == c and c != a):
            # for Isoceles triangle, exactly two sides must be same.
            return 'Isoscelene'

        if (a != b and b != c):
            # for scalene triangle, all three sides must be of different length.
            return 'Scalene'

        return 'NotATriangle'

    else:
        return 'NotATriangle'



def runClassifyTriangle(a, b, c):
    """ invoke classify_triangle with the specified arguments and print the result """
    print('classify_triangle(',a, ',', b, ',', c, ')=',classify_triangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework
