# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016

This file shows some simple (and buggy) python code to solve the Triangles assignment.   
The primary goal of this file is to demonstrate a simple python program and the use of the
unittest package.

Note that this code includes intentional errors for you to find.


@author: davejay1999
"""

import unittest     # this makes Python unittest module available

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
            return 'Isoceles'
        
        elif (a != b and b != c):
            # for scalene triangle, all three sides must be of different length.
            return 'Scalene'
        
        else:
            return 'NotATriangle'

    else:
        return 'NotATriangle'
    
        
        
def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(',a, ',', b, ',', c, ')=',classifyTriangle(a,b,c),sep="")


# The remainder of this code implements the unit test functionality

# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testSet1(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testMyTestOfZeroLengthSide(self):
        # with sides as length 0
        self.assertEqual(classifyTriangle(0,7,8),'InvalidInputTriangle','Invalid Triangle')
        self.assertEqual(classifyTriangle(0,0,65),'InvalidInputTriangle','Invalid Triangle')
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInputTriangle','Invalid Triangle')  

    def testMyTestOfTypesOfTriangle(self):
        # testcases of different type of triangle
        self.assertEqual(classifyTriangle(8,8,8),'Equilateral','8,8,8 should be equilateral')
        self.assertEqual(classifyTriangle(7,6,7),'Isoceles','Two equal sides so Isoceles triangle')
        self.assertEqual(classifyTriangle(13,12,5),'Right','It is a right triangle')
        self.assertEqual(classifyTriangle(0,7,8),'InvalidInputTriangle','Scalene triangle has all side different')
        self.assertNotEqual(classifyTriangle(100,8,101),'Equilateral','should be Scalene triangle')
        self.assertNotEqual(classifyTriangle(7,6,8),'Isoceles','should be Scalene triangle')
        self.assertNotEqual(classifyTriangle(13,12,5),'Scalene','It is a Right triangle')
        self.assertNotEqual(classifyTriangle(9,7,8),'NotATriangle','Scalene triangle has all side different')
         
    def testMyTestOfTrueCases(self): 
        # define multiple test sets to test different aspects of the code
        # notice that tests can have bugs too!
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        self.assertEqual(classifyTriangle(10,15,30),'NotATriangle','Invalid triangle')
        self.assertEqual(classifyTriangle(8,6,8),'Isoceles','Two equal sides so Isoceles triangle')
        self.assertEqual(classifyTriangle(13,12,5),'Right','It is a right triangle')
        self.assertEqual(classifyTriangle(9,7,8),'Scalene','Scalene triangle has all side different')

    def testMyTestOfFalseCases(self): 
        # define multiple test sets to test different aspects of the code
        self.assertNotEqual(classifyTriangle(10,10,10),'Isoceles','Should be Equilateral Triangle')
        self.assertNotEqual(classifyTriangle(10,10,8),'Scalene','Should be Isoceles Triangle')
        self.assertNotEqual(classifyTriangle(3,4,5),'NotATriangle','Should be Right Angle Triangle')

    def testMyTestOfInvalidTriangle(self):
        # testcases not following two side sum must be greater than third side condition
        self.assertEqual(classifyTriangle(0,7,8),'InvalidInputTriangle','Invalid Triangle')
        self.assertEqual(classifyTriangle(45,20,65),'NotATriangle','Should be Equilateral Triangle')
        self.assertNotEqual(classifyTriangle(49,100,52),'NotATriangle','Invalid Triangle')
        

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    
    # unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    
    
       
       
