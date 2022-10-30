def rect(x,y):
    if(x<0 or y<0): #W przypadku 0 prostokat bedzie linia
        return
    edge = "+---"
    segment = edge*x+"+\n"+"|   "*x+"|\n"
    wynik = segment*y+edge*x+"+\n"
    return wynik

x= int(input("Podaj szerokosc prosokata: "))
y= int(input("Podaj wyosokosc prosokata: "))


print(rect(x,y))
