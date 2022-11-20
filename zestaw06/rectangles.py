from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1>x2:
            x1 , x2 = x2, x1
        if y1>y2:
            y1,y2 = y2,y1
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return f"[({self.pt1.x}, {self.pt1.y}), ({self.pt2.x}, {self.pt2.y})]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.pt1 == other.pt1 and self.pt2 == other.pt2)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return Point(self.pt1.x + (abs(self.pt2.x-self.pt1.x)/2),self.pt1.y + (abs(self.pt2.y-self.pt1.y)/2))

    def area(self):            # pole powierzchni
        normal = (self.pt2-self.pt1)
        return normal.x*normal.y

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.pt1.x +x, self.pt1.y+y, self.pt2.x +x, self.pt2.y+y)


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r0 = Rectangle(0,0,0,0)
        self.r1 = Rectangle(0,0,1,1)
        self.r2 = Rectangle(-2,-2,6,8)
    def test_str(self):
        self.assertEqual(str(self.r1),"[(0, 0), (1, 1)]")
        self.assertEqual(str(self.r2),"[(-2, -2), (6, 8)]")
    def test_repr(self):
        self.assertEqual(repr(self.r1),"Rectangle(0, 0, 1, 1)")
        self.assertEqual(repr(self.r2),"Rectangle(-2, -2, 6, 8)")
    def test_eq(self):
        self.assertTrue((self.r1==self.r1))
        self.assertTrue(self.r2==self.r2)
        self.assertFalse((self.r1==self.r2))
    def test_ne(self):
        self.assertFalse((self.r1!=self.r1))
        self.assertFalse(self.r2!=self.r2)
        self.assertTrue((self.r1!=self.r2))
    def test_center(self):
        self.assertEqual(self.r0.center(),Point(0,0))
        self.assertEqual(self.r1.center(),Point(0.5,0.5))
        self.assertEqual(self.r2.center(),Point(2,3))
    def test_area(self):
        self.assertEqual(self.r1.area(), 1)
        self.assertEqual(self.r2.area(), 80)

    def test_move(self):
        self.assertEqual(self.r1.move(1,1),Rectangle(1,1,2,2))
        self.assertEqual(self.r2.move(2,2),Rectangle(0,0,8,10))
        self.assertEqual(self.r1.move(2,-5),Rectangle(2,-5,3,-4))




if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
