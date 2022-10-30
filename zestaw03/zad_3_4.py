wejscie = ""
while(wejscie!="stop"):
    wejscie = input("Podaj liczbe rzeczywista: ")
    try:
        print(wejscie+"^3 = "+str(pow(float(wejscie),3)))
    except ValueError:
        if(wejscie != "stop"):
            print("Wprowadzono napis zamiast liczby")
            