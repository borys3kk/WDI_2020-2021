def zad3_1():
    a = int(input("Podaj liczbe: "))
    b = 0
    d = a
    while a>0:
        c = a%2
        a = a//2
        b = b*2 + c

    if d==b:
        return True
    else:
        return False
print(zad3_1())