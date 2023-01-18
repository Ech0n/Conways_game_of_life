# Gra w Zycie
## na regulach Johna Conwaya

### Zasady gry
 Gra rozgrywa sie na pozornie nieskonczonej planszy. W rzeczywistosci jednak plansza jest rozmiaru najbardziej ekstremalnych punktow i dynamicznie sie rozszerza. Plansza sklada sie z komorek ktore maja dwa mozliwe stany: zywy i martwy. 
 Jezeli komorka jest zywa i ma 2 lub 3 sasiadow to w nastepnej generacji pozostanie zywa, a jesli nie to zmieni stan na martwy. 
 Jezeli komorka jest martwa i ma 3 sasiadow to w nastepnej generacji zmieni stan na zywa.
 Dwie komorki sasiaduja jezeli odleglosc pomiedzy nimi jest mniejsza niz 2.

### Uruchamianie:
```python main.py```
polecenie uruchamiajace program

Niektore parametry jak rozmiar startowy planszy oraz szybkosc rozgrywki mozna dostosowac zmienniajac odpowiednie zmienne na gorze pliku game.py

### Obsluga:
Program posiada 2 tryby (edytowania i gry).
### Tryb edytowania:
  Uzytkownik ma dostepna edytowalna plansze oraz 3 przyciski:
  + run - przechodzi w tryb gry
  + save - zapisuje obecna plansze do pliku
  + load - wczytuje plansze z pliku
  
###
Aby zmienic rozmiar planszy nalezy wczytac z pliku plansze okreslonego rozmiaru (np. 25x25)
W miare potrzeb monza tez stworzyc wlasny plik zapisu wiekszej planszy umieszczajac w jego 2 pierwszych linijkach wymiary.
### Tryb gry:
  Program wyswietla symulacje i pasek przypiety do dolu ekranu z napisem "RUNINNG" oznaczajacym ze program dziala w trybie gry oraz dwoma przyciskami pozwalajacymi zmienic tempo gry.
