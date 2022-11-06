def factorial(x:int) -> int:
    ret = 1
    for i in range(1,x+1):
        ret*=i
    return ret

x = int(input("Podaj liczbe: "))
print(factorial(x))