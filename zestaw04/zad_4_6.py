def sum_seq(L):
    suma = 0
    for a in L:
        if(isinstance(a,(list,tuple))):
            suma += sum_seq(a)
        else:
            suma += a
    return suma

krotka = (2,1,(1,8,3,(2,8,1,9),2),(2,11),2,11)
lista = [[23,51,11],[1],[11,31],20,13,[21,9],[8,0,9,[1,3,4,5,[2,9]]],15]

print(str(sum_seq(krotka)))
print(str(sum_seq(lista)))

