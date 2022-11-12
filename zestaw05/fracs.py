import math

def is_frac(frac):
    if len(frac)!=2:
        return False
    return isinstance(frac[0],int) and isinstance(frac[1],int)
    
def skroc(ulamek):
    nwd = math.gcd(ulamek[0],ulamek[1])
    ulamek = [int(ulamek[0]/nwd),int(ulamek[1]/nwd)]
    if ulamek[0]>0 and ulamek[1]<0:
        return [-ulamek[0],-ulamek[1]]
    return ulamek

def add_frac(frac1, frac2):        # frac1 + frac2
    if not is_frac(frac1) or not is_frac(frac2):
        return None
    ulamek = [frac1[0]*frac2[1]+frac2[0]*frac1[1],frac1[1]*frac2[1]]
    return skroc(ulamek)

def sub_frac(frac1, frac2):        # frac1 - frac2
    if not is_frac(frac1) or not is_frac(frac2):
        return None
    ulamek = [frac1[0]*frac2[1]-frac2[0]*frac1[1],frac1[1]*frac2[1]]
    return skroc(ulamek)

def mul_frac(frac1, frac2):        # frac1 * frac2
    if not is_frac(frac1) or not is_frac(frac2):
        return None
    ulamek = [frac1[0]*frac2[0],frac1[1]*frac2[1]]
    return skroc(ulamek)

def div_frac(frac1, frac2):        # frac1 / frac2
    if not is_frac(frac1) or not is_frac(frac2):
        return None
    ulamek = [frac1[0]*frac2[1],frac1[1]*frac2[0]]
    return skroc(ulamek)

def is_positive(frac):             # bool, czy dodatni
    if not is_frac(frac):
        return None
    return frac[0]*frac[1]>0

def is_zero(frac):                 # bool, typu [0, x]
    return frac[0]==0

def cmp_frac(frac1, frac2):        # -1 | 0 | +1
    ratio1 = frac1[0]/frac1[1] 
    ratio2 = frac2[0]/frac2[1]
    if( ratio1 == ratio2): return 0
    if( ratio1 < ratio2): return -1
    else: return 1


def frac2float(frac):
    return frac[0]/frac[1] 

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 5], [-2, 7]), [11, 35])
        self.assertEqual(add_frac(self.zero, [1, 3]), [1, 3])
        self.assertEqual(add_frac(self.zero, self.zero), self.zero)

        self.assertEqual(add_frac([5, 3], [4, 7]), [47, 21])
        self.assertEqual(add_frac([46, -21], [-29, 7]), [-19, 3])


    def test_sub_frac(self): 
        self.assertEqual(sub_frac(self.zero,self.zero),self.zero)
        self.assertEqual(sub_frac(self.zero,[5,3]),[-5,3])
        self.assertEqual(sub_frac([2,5],self.zero),[2,5])
        self.assertEqual(sub_frac([4,3],[1,3]),[1,1])
        self.assertEqual(sub_frac([-4,3],[1,2]),[-11,6])




    def test_mul_frac(self): 
        self.assertEqual(mul_frac(self.zero,self.zero),self.zero)
        self.assertEqual(mul_frac(self.zero,[4,2]),self.zero)
        self.assertEqual(mul_frac([2,1],[4,2]),[4,1])
        self.assertEqual(mul_frac([3,7],[2,5]),[6,35])
        self.assertEqual(mul_frac([2,-3],[5,-2]),[5,3])

    def test_div_frac(self): 
        self.assertEqual(div_frac(self.zero,[4,2]),self.zero)
        self.assertEqual(div_frac([20,3],[4,2]),[10,3])
        self.assertEqual(div_frac([5,3],[7,2]),[10,21])
        self.assertEqual(div_frac([-3,7],[-1,-3]),[-9,7])


    def test_is_positive(self):
        self.assertEqual(is_positive([2,4]),True)
        self.assertEqual(is_positive([-1,-5]),True)
        self.assertEqual(is_positive([1,-5]),False)
        self.assertEqual(is_positive([-1,5]),False)



    def test_is_zero(self):
        self.assertEqual(is_zero(self.zero),True)
        self.assertEqual(is_zero([0,0]),True)
        self.assertEqual(is_zero([2,3]),False)
        self.assertEqual(is_zero([-41,13]),False)
        self.assertEqual(is_zero([0,13]),True)




    def test_cmp_frac(self): 
        self.assertEqual(cmp_frac([2,1],[4,2]),0)
        self.assertEqual(cmp_frac([3,7],[9,21]),0)
        self.assertEqual(cmp_frac([52,6],[-4,2]),1)
        self.assertEqual(cmp_frac([2,11],[4,2]),-1)


    def test_frac2float(self):
        self.assertEqual(frac2float(self.zero),0.0)
        self.assertEqual(frac2float([1,2]),0.5)
        self.assertEqual(frac2float([2,5]),0.4)
        self.assertEqual(frac2float([-2,5]),-0.4)
        self.assertEqual(frac2float([9,10]),0.9)
        self.assertEqual(frac2float([-5,2]), -2.5)



    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy