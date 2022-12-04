from rectangles import Rectangle
from points import Point
import pytest

class TestRectangle:
    @pytest.fixture
    def r0(self):
        return Rectangle(0,0,0,0)
    @pytest.fixture
    def r1(self):
        return Rectangle(0,0,1,1)
    @pytest.fixture
    def r2(self):
        return Rectangle(-2.0,-2.0,6.0,8.0)
    @pytest.fixture
    def r3(self):
        return Rectangle(0.0,0.0,4.0,6.0)
    @pytest.fixture
    def r4(self):
        return Rectangle(3.0,2.0,9.0,11.0)
    @pytest.fixture
    def r5(self):
        return Rectangle(-1.0,1.4,2.1,4.5)

    def test_str(self,r1,r2):
        assert str(r1) == "[(0, 0), (1, 1)]"
        assert str(r2) == "[(-2.0, -2.0), (6.0, 8.0)]"
    def test_repr(self,r1,r2):
        assert repr(r1) == "Rectangle(0, 0, 1, 1)"
        assert repr(r2) == "Rectangle(-2.0, -2.0, 6.0, 8.0)"
    def test_eq(self,r1,r2):
        assert (r1==r1) == True
        assert (r2==r2) == True
        assert (r1==r2) == False
    def test_ne(self,r1,r2):
        assert (r1!=r1) == False
        assert (r2!=r2) == False
        assert (r1!=r2) == True
    def test_area(self,r1,r2):
        assert r1.area() == 1
        assert r2.area() == 80
    def test_move(self,r1,r2):
        assert r1.move(1,1) == Rectangle(1,1,2,2)
        assert r2.move(2,2) == Rectangle(0,0,8,10)
        assert r1.move(2,-5) == Rectangle(2,-5,3,-4)
    def test_intersetion(self,r1,r2,r3,r4,r5):
        assert r3.intersection(r4) == Rectangle(3,2,4,6)
        assert r1.intersection(r3) == Rectangle(0,0,1,1)
        assert r1.intersection(r4) == False
        assert r4.intersection(r2) == Rectangle(3,2,6,8)
        assert r3.intersection(r5) == Rectangle(0.0,1.4,2.1, 4.5)
    def test_cover(self,r1,r2,r3,r4):
        assert r2.cover(r4) == Rectangle(-2,-2,9,11)
        assert r1.cover(r4) == Rectangle(0,0,9,11)
        assert r3.cover(r2) == r2
    @pytest.fixture
    def rect4_1(self):
        r1 = Rectangle(-2.0,-2.0,2.0,3.0)
        r2 = Rectangle(2.0,3.0,6.0,8.0)
        r3 = Rectangle(2.0,-2.0,6.0,3.0)
        r4 = Rectangle(-2.0,3.0,2.0,8.0)
        return (r1,r2,r3,r4) 
    @pytest.fixture
    def rect4_2(self):
        r1 = Rectangle(0,0,0.5,0.5)
        r2 = Rectangle(0.5,0.5,1,1)
        r3 = Rectangle(0.5,0,1,0.5)
        r4 = Rectangle(0,0.5,0.5,1)
        return (r1,r2,r3,r4)
    def test_make4(self,r2,r1,rect4_1,rect4_2):
        assert (r2.make4()) == rect4_1
        assert r1.make4() == rect4_2
    def test_center(self,r0,r1,r2):
        assert r0.center == Point(0,0)
        assert r1.center == Point(0.5,0.5)
        assert r2.center == Point(2,3) 
    def test_properties(self,r4,r5):
        assert r4.top == 11.0
        assert r4.top != 4
        assert r5.left == -1.0
        assert r5.bottom == 1.4
        assert r5.bottomleft == Point(-1,1.4)
        assert r5.bottomright == Point(2.1,1.4)
    @pytest.fixture
    def p1(self):
        return Point(0,0)
    @pytest.fixture
    def p2(self):
        return Point(1,1)
    @pytest.fixture
    def p3(self):
        return Point(4,6)
    def test_from_points(self,p1,p2,p3,r1,r3):
        assert Rectangle.from_points((p1,p2)) == r1
        assert Rectangle.from_points((p1,p3)) == r3

if __name__ == '__main__':
    pytest.main()     # uruchamia wszystkie testy
