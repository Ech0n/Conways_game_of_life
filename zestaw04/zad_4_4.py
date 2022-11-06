def fibonacci(n):
    if n<=0:
        raise ValueError("Argument out of range!")
    x = 1
    y = 1
    for _ in range(int(n-2)):
        y = x + y
        x = y - x
    return y

n = int(input("Podaj liczbe n: "))
print(str(fibonacci(n)))
