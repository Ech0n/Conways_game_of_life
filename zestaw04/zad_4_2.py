def rect(x,y):
    if(x<0 or y<0): #W przypadku 0 prostokat bedzie linia
        return
    edge = "+---"
    segment = edge*x+"+\n"+"|   "*x+"|\n"
    wynik = segment*y+edge*x+"+\n"
    return wynik

def miarka(x):
    if(dlugosc > 0):
        return (("|...."*dlugosc)+"|\n0") + "".join([str(i+1).rjust(5) for i in range(dlugosc)])
    return "Bledne dane!"

dlugosc = int(input("Podaj dlugosc miarki: "))

print(miarka(dlugosc))


x= int(input("Podaj szerokosc prosokata: "))
y= int(input("Podaj wyosokosc prosokata: "))

print(rect(x,y))
