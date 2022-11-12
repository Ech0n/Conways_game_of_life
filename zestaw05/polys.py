def add_poly(poly1, poly2):       # poly1(x) + poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)+(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]


def sub_poly(poly1, poly2):         # poly1(x) - poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)-(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]


def mul_poly(poly1, poly2):        # poly1(x) * poly2(x)
    warunek=lambda i:((poly1[i] if (i<len(poly1)) else 0)*(poly2[i] if (i<len(poly2)) else 0))
    return [ warunek(i) for i in range(max(len(poly1),len(poly2)))]

def is_zero(poly):                 # bool, [0], [0,0], itp.
    for a in poly:
        if a != 0:
            return False
        return True
def eq_poly(poly1, poly2):       # bool, porównywanie poly1(x) == poly2(x)
    return poly1==poly2
def eval_poly(poly, x0): pass           # poly(x0), algorytm Hornera

def combine_poly(poly1, poly2): pass    # poly1(poly2(x)), trudne!

def pow_poly(poly, n): pass             # poly(x) ** n

def diff_poly(poly): pass               # pochodna wielomianu


p1 = [2, 1]                   # W(x) = 2 + x
p2 = [2, 1, 0]                # jw  (niejednoznaczność)
p3 = [-3, 0, 1]               # W(x) = -3 + x^2
p4 = [3]                      # W(x) = 3, wielomian zerowego stopnia
p5 = [0]                      # zero
p6 = [0, 0, 0]                # zero (niejednoznaczność)

print(add_poly(p1,p3))
print(sub_poly(p1,p3))
print(mul_poly(p1,p3))
