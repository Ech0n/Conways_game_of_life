# Gra w Życie
## na regułach Johna Conwaya

### Zasady gry
 Gra rozgrywa się na pozornie nieskończonej planszy. W rzeczywistości jednak plansza jest rozmiaru najbardziej ekstremalnych punktów i dynamicznie się rozszerza. Plansza składa się z komórek które maja dwa możliwe stany: żywy i martwy. 
 Jeżeli komórka jest żywa i ma 2 lub 3 sąsiadów to w następnej generacji pozostanie żywa, a jeśli nie to zmieni stan na martwy. 
 Jeżeli komórka jest martwa i ma 3 sąsiadów to w następnej generacji zmieni stan na żywą.
 Dwie komórki sąsiadują jeżeli odległość pomiędzy nimi jest mniejsza niż 2.

### Uruchamianie:
```python game.py```
polecenie uruchamiające program

Niektóre parametry jak rozmiar startowy planszy oraz szybkość rozgrywki można dostosować zmieniając odpowiednie zmienne na górze pliku game.py

### Obsługa:
Program posiada 2 tryby (edytowania i gry).
### Tryb edytowania:
  Użytkownik ma dostępna edytowalna plansze oraz 3 przyciski:
  + run - przechodzi w tryb gry
  + save - zapisuje obecna plansze do pliku
  + load - wczytuje plansze z pliku
  Edytowalna plansza:
    Po uruchomieniu programu użytkownik widzi plansze w rozmiarze domyślnym. Plansza składa sie z komórek na siatce na które można kliknąć co zmienia ich stan.
  
###
Aby zmienić rozmiar planszy należy wczytać z pliku zapisu plansze określonego rozmiaru (np. 25x25)
W miarę potrzeb można tez stworzyć własny plik zapisu większej planszy. W tym celu należy utworzyć dowolny plik tekstowy i w dowolnym edytorze umieścić w dwóch pierwszych linijkach wymiary, a pozostałe linijki zostawić puste.
### Tryb gry:
  Program wyświetla symulacje i pasek przypięty do dołu ekranu z napisem "RUNINNG" oznaczającym ze program działa w trybie gry oraz dwoma przyciskami pozwalającymi zmienić tempo gry.
