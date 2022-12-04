from points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1>x2 or y1>y2:
            raise Exception("Podano zle wspolrzedne Prostokata!")
        self.__pt1 = Point(x1, y1)
        self.__pt2 = Point(x2, y2)

    def __str__(self):         # "[(x1, y1), (x2, y2)]"
        return f"[({self.__pt1.x}, {self.__pt1.y}), ({self.__pt2.x}, {self.__pt2.y})]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.__pt1.x}, {self.__pt1.y}, {self.__pt2.x}, {self.__pt2.y})"

    def __eq__(self, other):   # obsługa rect1 == rect2
        return (self.__pt1 == other.bottomleft and self.__pt2 == other.topright)

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    @property
    def center(self):          # zwraca środek prostokąta
        return Point(self.__pt1.x + (abs(self.__pt2.x-self.__pt1.x)/2),self.__pt1.y + (abs(self.__pt2.y-self.__pt1.y)/2))

    def area(self):            # pole powierzchni
        normal = (self.__pt2-self.__pt1)
        return normal.x*normal.y

    def move(self, x, y):      # przesunięcie o (x, y)
        return Rectangle(self.__pt1.x +x, self.__pt1.y+y, self.__pt2.x +x, self.__pt2.y+y)

    def intersection(self, other): # część wspólna prostokątów
        #Ustalamy czy przeciecie istnieje
        if not(self.left <= other.right and 
            self.right >= other.left and
            self.top >= other.bottom and
            self.bottom <= other.top):
            return False 
        
        minx = min(self.right,other.right)
        maxx = max(self.left,other.left)
        miny = min(self.top,other.top)
        maxy = max(self.bottom,other.bottom)

        return Rectangle(maxx,maxy,minx,miny)

    def cover(self, other):    # prostąkąt nakrywający oba
        p1 = Point(min(self.left,other.left),min(self.bottom,other.bottom))
        p2 = Point(max(self.right,other.right),max(self.top,other.top))
        return Rectangle(p1.x,p1.y,p2.x,p2.y)

    def make4(self):          # zwraca krotkę czterech mniejszych
        middle = Point(self.__pt1.x + (abs(self.__pt2.x-self.__pt1.x)/2),self.__pt1.y + abs(self.__pt2.y-self.__pt1.y)/2)
        rect1 = Rectangle(self.__pt1.x,self.__pt1.y,middle.x,middle.y,)
        rect2 = Rectangle(middle.x,middle.y,self.__pt2.x,self.__pt2.y)
        rect3 = Rectangle(middle.x,self.__pt1.y,self.__pt2.x,middle.y)
        rect4 = Rectangle(self.__pt1.x,middle.y,middle.x,self.__pt2.y)
        return (rect1,rect2,rect3,rect4)

    @classmethod
    def from_points(cls,points): #metoda klasy
        if not isinstance(points[0],(Point)) or not isinstance(points[1],(Point)):
            raise ValueError("Konstruktor from_points otrzymal zly argument")
        return cls(points[0].x,points[0].y,points[1].x,points[1].y)

    @property
    def top(self):
        return self.__pt2.y

    @property
    def bottom(self):
        return self.__pt1.y

    @property
    def left(self):
        return self.__pt1.x

    @property
    def right(self):
        return self.__pt2.x

    @property
    def width(self):
        return abs(self.__pt2.x-self.__pt1.x)

    @property
    def heigth(self):
        return abs(self.__pt2.y-self.__pt1.y)

    @property
    def topleft(self):
        return Point(self.__pt1.x,self.__pt2.y)
    @property
    def topright(self):
        return self.__pt2
    @property
    def bottomleft(self):
        return self.__pt1
    @property
    def bottomright(self):
        return Point(self.__pt2.x,self.__pt1.y)
