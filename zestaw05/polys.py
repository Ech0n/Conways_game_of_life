def add_poly(poly1, poly2):       # poly1(x) + poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)+(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]


def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)-(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]


def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    wynik = [0 for _ in range(len(poly1)+len(poly2)-1)]
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            wynik[i+j] += poly1[i]*poly2[j]
    return wynik
        

def is_zero(poly):                 # bool, [0], [0,0], itp.
    for a in poly:
        if a != 0:
            return False
    return True
def eq_poly(poly1, poly2):       # bool, porównywanie poly1(x) == poly2(x)
    if(is_zero(poly1) and is_zero(poly2)):
        return True
    return poly1==poly2
def eval_poly(poly, x0):           # poly(x0), algorytm Hornera
    wynik = 0
    for n in range(len(poly)-1,-1,-1):
        wynik = wynik*x0 + poly[n]
    return wynik

def num_to_poly(num,n):
    wynik = [0 for _ in range(n+1)]
    wynik[n] = num
    return wynik

def remove_aditional_zeros(poly):
    for i in range(len(poly)-1,-1,-1):
        if poly[i]!=0:
            return poly
        else:
            poly.pop()

def mul_el_poly(poly1, poly2):       # poly1(x) + poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)*(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]


def combine_poly(poly1, poly2):    # poly1(poly2(x)), trudne!
    pass
    # wynik = []
    # for n in range(len(poly1)-1,-1,-1):
    #     print(mul_poly( wynik , poly2 ), num_to_poly(poly1[n],n), add_poly( mul_poly( wynik , poly2 ), num_to_poly(poly1[n],n)))
    #     wynik = add_poly( mul_poly( wynik , poly2 ), num_to_poly(poly1[n],n) )
    # return wynik
    
def pow_poly(poly, n):             # poly(x) ** n
    if n == 0:
        return [1]
    wynik = poly
    for i in range(n-1):
        wynik = mul_poly(wynik,poly)
    return wynik

def diff_poly(poly):               # pochodna wielomianu
    wynik = [0 for _ in range(len(poly)-1)]
    for i in range(1,len(poly)):
        wynik[i-1] = poly[i]*i
    return wynik


p1 = [2, 1]                   # W(x) = 2 + x
p2 = [2, 1, 0]                # jw  (niejednoznaczność)
p3 = [-3, 0, 1]               # W(x) = -3 + x^2
p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
p5 = [0]                      # zero
p6 = [0, 0, 0]                # zero (niejednoznaczność)

import unittest

class TestPolynomials(unittest.TestCase):

    def setUp(self):
        self.p1 = [0, 1]      # W(x) = x
        self.p2 = [0, 0, 1]   # W(x) = x^2
        self.p3 = [1,1,1]     # x^2 + x + 1
        self.p4 = [3,2,1]     # x^2 + 2x + 3
        self.p5 = [2,1,1]
        self.p6 = [1,1]

        self.zero1 = [0]      # zero
        self.zero2 = [0, 0, 0]

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p2,self.p1),[0,-1,1])

    def test_mul_poly(self): 
        self.assertEqual(mul_poly(self.p2,self.p1),[0,0,0,1])
        self.assertEqual(mul_poly(self.p3,self.p1),[0,1,1,1])
        self.assertEqual(mul_poly(self.p2,self.p3),[0,0,1,1,1])

    def test_is_zero(self): 
        self.assertEqual(is_zero(self.zero1),True)
        self.assertEqual(is_zero(self.zero2),True)
        self.assertEqual(is_zero(self.p2),False)

    def test_eq_poly(self): 
        self.assertEqual(eq_poly(self.p1,self.p1),True)
        self.assertEqual(eq_poly(self.p2,self.p2),True)
        self.assertEqual(eq_poly(self.zero1,self.zero2),True)
        self.assertEqual(eq_poly(self.p1,self.p2),False)

    def test_eval_poly(self): 
        self.assertEqual(eval_poly(self.p3,1),3)
        self.assertEqual(eval_poly(self.p3,2),7)
        self.assertEqual(eval_poly(self.p3,-2),3)
        self.assertEqual(eval_poly(self.p3,-2),3)
        self.assertEqual(eval_poly(self.p4,2),11)
        self.assertEqual(eval_poly(self.p4,-2),3)

    def test_combine_poly(self): 
        # self.assertEqual(combine_poly([1],[1]),[1])
        # self.assertEqual(combine_poly([0,1],[1]),[0,1])
        # self.assertEqual(combine_poly([0,1],[0,1]),[0,0,1])
        # self.assertEqual(combine_poly(self.p1,self.p2),[0,0,0,1])
        # self.assertEqual(combine_poly(self.p5,self.p6),[4,3,1])
        # self.assertEqual(combine_poly(self.p3,self.p3),[1,2,3,2,1])
        # self.assertEqual(combine_poly(self.p3,self.p2),[1,0,0,1,1])
        pass

    def test_pow_poly(self):
        self.assertEqual(pow_poly(self.p3,2),[1,2,3,2,1])

    def test_diff_poly(self): 
        self.assertEqual(diff_poly(self.p2),[0,2])
        self.assertEqual(diff_poly(self.p1),[1])
        self.assertEqual(diff_poly(self.p3),[1,2])


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy