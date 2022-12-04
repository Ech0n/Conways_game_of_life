import math


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):         # zwraca string "(x, y)"
        return f"({self.x}, {self.y})"

    def __repr__(self):        # zwraca string "Point(x, y)"
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x+other.x,self.y+other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x-other.x,self.y-other.y)


    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        if(isinstance(other,(int,float))):
            return Point(self.x*other,self.y*other)
        return (self.x*other.x)+(self.y*other.y)


    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return float(math.sqrt(self.x**2+self.y**2))

    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.

import unittest

class TestPoint(unittest.TestCase): 
    def setUp(self):
        self.x0 = 0
        self.x1 = 5
        self.x2 = -2
        
        self.y0 = 0
        self.y1 = 3
        self.y2 = -4

        self.p0 = Point(self.x0,self.y0)
        self.p1 = Point(self.x2,self.y1) #(-2,3)
        self.p2 = Point(self.x2,self.y2) #(-2,-4)

    def test_str(self):
        self.assertEqual(str(self.p0),"(0, 0)")
        self.assertEqual(str(self.p1),"(-2, 3)")

    def test_repr(self):
        self.assertEqual(repr(self.p0),"Point(0, 0)")
        self.assertEqual(repr(self.p1),"Point(-2, 3)")
    def test_eq(self):
        self.assertEqual(self.p0,Point(0,0))
        self.assertEqual(self.p0==self.p1,False)
    def test_ne(self):
        self.assertEqual(self.p0!=Point(0,0),False)
        self.assertEqual(self.p0!=self.p1,True)
    def test_add(self):
        self.assertEqual(self.p0+self.p1,Point(-2,3))
        self.assertEqual(self.p2+self.p1,Point(-4,-1))
        self.assertEqual(self.p1+self.p1+self.p1+self.p1,Point(-8,12))
    def test_sub(self):
        self.assertEqual(self.p0-self.p1,Point(2,-3))
        self.assertEqual(self.p2-self.p1,Point(0,-7))
        self.assertEqual(self.p1-self.p1-self.p1-self.p1,Point(4,-6))
    def test_mul(self):
        self.assertEqual(self.p0*self.p1,0)
        self.assertEqual(self.p2*self.p1,-8)
        self.assertEqual(self.p1*self.p1, 13 )
        self.assertEqual(self.p1*2, Point(-4,6) )
    def test_cross(self):
        self.assertEqual(Point.cross(self.p1,self.p2),14)
        self.assertEqual(Point.cross(self.p2,self.p2),0)

    def test_length(self):
        self.assertEqual(Point(3,4).length(),5)
        self.assertEqual(Point(8,6).length(),10)
    def test_hash(self):
        self.assertEqual(hash(Point(2,9)),hash(Point(2,9)))
    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
