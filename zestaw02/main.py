line = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Morbi nisl neque, luctus eu pretium sit amet, scelerisque eu dui.
 Donec sed venenatis leo.
 Pellentesque a pretium libero.
 Duis eu vulputate urna.
 Donec GvR est turpis, euismod at quam eget, dictum condimentum nisi."""

word = "jakiesslowo"

#zadanie 2_10
print("-------------------------\nzadanie 2.10:")

print("Liczba wyrazow w line:")
#sposob 1:
print(len(line.split(' ')))

#sposob 2:
print(line.count(' ')+1)

###################
#zadanie 2_11
print("-------------------------\nzadanie 2.11:")


for e in word[:-1]:
    print(e,end='_')
print(word[-1])

######################
#zadanie 2_12
print("-------------------------\nzadanie 2.12:")

pierwsze = ""
ostatnie = ""
for wyraz in line.replace("\n","").split(' '):
    pierwsze += wyraz[0]
    ostatnie += wyraz[-1]

print("Wyraz z pierwszych znakow: "+pierwsze+"\nWyraz z ostatnich znakow: "+ostatnie)

###################
#zadanie 2_13
print("-------------------------\nzadanie 2.13:")

ile = sum(len(a) for a in line.split(' '))
print("Suma dlugosci wyrazow: "+str(ile))

####################
#zadanie 2_14
print("-------------------------\nzadanie 2.14:")

najdluzszy = max(len(a) for a in line.split(' '))
index = [len(a) for a in line.split(' ')].index(najdluzszy)
print("Najdzluzszy wyraz to "+line.split(' ')[index]+", a jego dlugosc to: "+str(najdluzszy+1))

####################
#zadanie 2_15
print("-------------------------\nzadanie 2.15:")

L = [a for a in range(2,20,3)]
napis = ""
for liczba in L:
    napis += str(liczba)

print("Ciag cyfr stworzony z liczb z tablicy L: "+napis)

#######################
#zadanie 2_16
print("-------------------------\nzadanie 2.16:")
print("GvR zamienione na Guido van Rossum:")
print(line.replace("GvR","Guido van Rossum"))

#########################
#zadanie 2_17
print("-------------------------\nzadanie 2.17:")
print("Posortowane alfabetycznie:")
print(sorted(line.split(" ")))
print("Posortowane po dlugosci:")
print(sorted(line.split(" "),key=len))

######################
#zadanie 2_18
print("-------------------------\nzadanie 2.18:")
import random
i = random.randint(100000000000000000,100000000000000000000000)
print("ile 0 w liczbie "+str(i)+": "+str(str(i).count("0")))

######################
#zadanie 2_18
print("-------------------------\nzadanie 2.19:")
L = [random.randint(1,200) for _ in range(40)]
for e in L:
    print(str(e).zfill(3),end = ' ')
