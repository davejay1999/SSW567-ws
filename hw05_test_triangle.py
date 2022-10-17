# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: author1
@author: JayDave
"""

import unittest

from hw05_classify_triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classify_triangle(10,10,10),'Equilateral','10,10,10 should be equilateral')
        
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classify_triangle(9,9,9),'Equilateral','9,9,9 should be equilateral')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classify_triangle(1,2,2.5),'Scalene','1,2,2.5 is a Scalene triangle')

    def testIsosceleneTrianglesA(self): 
        self.assertEqual(classify_triangle(1,12,12),'Isoscelene','1,12,12 is a Isoscelene')
        
    def testIsosceleneTrianglesB(self): 
        self.assertEqual(classify_triangle(10,9,10),'Isoscelene','10,9,10 should be Isoscelene')

    def testIsNotATriangleA(self): 
        self.assertEqual(classify_triangle(6,2,4),'NotATriangle','6,2,4 is a NotATriangle')

    def testIsNotATriangleB(self): 
        self.assertEqual(classify_triangle(5,6,12),'NotATriangle','5,6,12 is a NotATriangle')
        
    def testInvalidInputTriangleA(self): 
        self.assertEqual(classify_triangle(0,0,2),'InvalidInputTriangle','0,0,2 should be InvalidInputTriangle')

    def testInvalidInputTriangleB(self): 
        self.assertEqual(classify_triangle(0,-6,10),'InvalidInputTriangle','0,-6,10 should be InvalidInputTriangle')

    def testInvalidInputTriangleC(self): 
        self.assertEqual(classify_triangle(0,0,0),'InvalidInputTriangle','0,0,0 should be InvalidInputTriangle')
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

