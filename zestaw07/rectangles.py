from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1>x2 or y1>y2:
            raise Exception("Podano zle wspolrzedne Prostokata!")
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



    def intersection(self, other): # część wspólna prostokątów
        #Ustalamy czy przeciecie istnieje
        if not(self.pt1.x <= other.pt2.x and 
            self.pt2.x >= other.pt1.x and
            self.pt2.y >= other.pt1.y and
            self.pt1.y <= other.pt2.y):
            return False 
        
        minx = min(self.pt2.x,other.pt2.x)
        maxx = max(self.pt1.x,other.pt1.x)
        miny = min(self.pt2.y,other.pt2.y)
        maxy = max(self.pt1.y,other.pt1.y)

        return Rectangle(maxx,maxy,minx,miny)

    def cover(self, other):    # prostąkąt nakrywający oba
        p1 = Point(min(self.pt1.x,other.pt1.x),min(self.pt1.y,other.pt1.y))
        p2 = Point(max(self.pt2.x,other.pt2.x),max(self.pt2.y,other.pt2.y))
        return Rectangle(p1.x,p1.y,p2.x,p2.y)

    def make4(self):          # zwraca krotkę czterech mniejszych
        middle = Point(self.pt1.x + (abs(self.pt2.x-self.pt1.x)/2),self.pt1.y + abs(self.pt2.y-self.pt1.y)/2)
        rect1 = Rectangle(self.pt1.x,self.pt1.y,middle.x,middle.y,)
        rect2 = Rectangle(middle.x,middle.y,self.pt2.x,self.pt2.y)
        rect3 = Rectangle(middle.x,self.pt1.y,self.pt2.x,middle.y)
        rect4 = Rectangle(self.pt1.x,middle.y,middle.x,self.pt2.y)
        return (rect1,rect2,rect3,rect4)


# Kod testujący moduł.

import unittest

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r0 = Rectangle(0,0,0,0)
        self.r1 = Rectangle(0,0,1,1)
        self.r2 = Rectangle(-2.0,-2.0,6.0,8.0)
        self.r3 = Rectangle(0.0,0.0,4.0,6.0)
        self.r4 = Rectangle(3.0,2.0,9.0,11.0)
        self.r5 = Rectangle(-1.0,1.4,2.1,4.5)

    def test_str(self):
        self.assertEqual(str(self.r1),"[(0, 0), (1, 1)]")
        self.assertEqual(str(self.r2),"[(-2.0, -2.0), (6.0, 8.0)]")
    def test_repr(self):
        self.assertEqual(repr(self.r1),"Rectangle(0, 0, 1, 1)")
        self.assertEqual(repr(self.r2),"Rectangle(-2.0, -2.0, 6.0, 8.0)")
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
    def test_intersetion(self):
        self.assertEqual(self.r3.intersection(self.r4),Rectangle(3,2,4,6))
        self.assertEqual(self.r1.intersection(self.r3),Rectangle(0,0,1,1))
        self.assertEqual(self.r1.intersection(self.r4),False)
        self.assertEqual(self.r4.intersection(self.r2),Rectangle(3,2,6,8))
        self.assertEqual(self.r3.intersection(self.r5),Rectangle(0.0,1.4,2.1, 4.5))

    def test_cover(self):
        self.assertEqual(self.r2.cover(self.r4),Rectangle(-2,-2,9,11))
        self.assertEqual(self.r1.cover(self.r4),Rectangle(0,0,9,11))
        self.assertEqual(self.r3.cover(self.r2),self.r2)

    def test_make4(self):
        self.assertEqual((self.r2.make4()),
         (Rectangle(-2.0,-2.0,2.0,3.0),Rectangle(2.0,3.0,6.0,8.0),
        Rectangle(2.0,-2.0,6.0,3.0),Rectangle(-2.0,3.0,2.0,8.0)) )
        self.assertEqual(self.r1.make4(),
        (Rectangle(0,0,0.5,0.5),Rectangle(0.5,0.5,1,1),Rectangle(0.5,0,1,0.5),Rectangle(0,0.5,0.5,1)) )


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
