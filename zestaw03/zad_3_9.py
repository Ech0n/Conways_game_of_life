sekwencja = [[],[4],(1,2),[3,4],(5,6,7)]
wynik = [sum(x) for x in sekwencja]

print(wynik)
assert wynik == [0,4,3,7,18]

