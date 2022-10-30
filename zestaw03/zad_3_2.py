#zadanie 3.2
# Funkcja tablica.sort() nie zwraca zadnej wartosci tylko operuje na danej tablicy
# L = [3, 5, 4] ; L = L.sort()
# poprwana wersja:
L = [3, 5, 4] ; L.sort()

# Bledna wersja, przypisujemy 3 wartosci do 2 zmiennych
# x, y = 1, 2, 3
# Poprawna wersja
x , y = 1 ,2

#Bledna wersja, X nie jest tablica (jest tuple)
# X = 1, 2, 3 ; X[1] = 4
# Poprawana wersja
X =[1, 2, 3 ]; X[1] = 4

# Bledna wersja, X ma rozmiar 3 wiec nie mozemy przypisac do elementu o indexie 3 (4 element tablicy)
# X = [1, 2, 3] ; X[3] = 4
# Poprawana wersja:
X = [1, 2, 3] ; X[2] = 4

# Bledna wersja, w python string nie jest tablica nie mozna uzyc funkcji append
# X = "abc" ; X.append("d")
#Poprawna wersja
X = "abc" ; X += "d"

#Blenda wersja, funkcja pow przyjmuje 2 argumenty wiec potrzebujemy dodatkowy argument
#L = list(map(pow, range(8)))
# Poprawna wersja,Zamiast range(8) mozna dac jaka kolwiek tablice 8 argumentow
L = list(map(pow, range(8),range(8)))
# 
