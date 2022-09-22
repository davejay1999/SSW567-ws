# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a,b,c):
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
        
        elif a == b and b == c:
            # for  Equilateral triangle, it must satify side_1 = side_2 = side_3.
            return 'Equilateral'
        
        elif (a == b and b != c) or (a == c and a != b) or (b == c and c != a):
            # for Isoceles triangle, exactly two sides must be same.
            return 'Isoscelene'
        
        elif (a != b and b != c):
            # for scalene triangle, all three sides must be of different length.
            return 'Scalene'
        
        else:
            return 'NotATriangle'

    else:
        return 'NotATriangle'
    
        
              
        