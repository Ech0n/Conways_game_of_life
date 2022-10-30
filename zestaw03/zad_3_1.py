#zadanie 3.1
# 
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
# Kod jest poprawny aczkolwiek warunek ifa nigdy nie zostanie spelniony
#
# for i in "axby": if ord(i) < 100: print (i)
# Kod nie jest poprawny gdyz python wymaga nowych linij i poprawnych tabulacji w przypadku wiecej niz dwoch lini polecen

for i in "axby": print (ord(i) if ord(i) < 100 else i)
#Kod jest poprawny gdyz po dwukropku znajduje sie pojedyncza linijka
