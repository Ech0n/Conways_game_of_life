import itertools
import random

print("Iterator 0,1,0,1,0...")
zerojedynki = itertools.cycle([0,1])
for i in range(10):
    print(next(zerojedynki),end=", ")

print("\nIterator losujacy z ['N','E','S','W']: ")
nesw =  (random.choice(["N","E","S","W"]) for _ in iter(int, 1))
for i in range(10):
    print(next(nesw),end=", ")

print("\nIterator losujacy dni numery dni tygodnia")
dnitygodnia =  (random.choice(range(7)) for _ in iter(int, 1))
for i in range(10):
    print(next(dnitygodnia),end=",")
print()