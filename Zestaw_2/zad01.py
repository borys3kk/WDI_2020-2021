def zad1(liczba):
    f1, f2 = 1, 1
    while True:
        if liczba == f1*f2:
            return True
        elif f1*f2 > liczba:
            return False
        else:
            f1,f2 = f1+f2,f1

print(zad1(int(input("Podaj liczbe: "))))