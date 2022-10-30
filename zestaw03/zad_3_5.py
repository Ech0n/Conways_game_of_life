dlugosc = int(input("Podaj dlugosc miarki: "))
if(dlugosc > 0):
    miarka = (("|...."*dlugosc)+"|\n0") + "".join([str(i+1).rjust(5) for i in range(dlugosc)])
print(miarka)