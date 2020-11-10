from math import log
from math import ceil

def zad1():
    hex = "0123456789ABCDEF"
    liczba = int(input('Liczba >> '))
    podstawa = int(input('Podstawa >> '))

    tab = [0 for _ in range(int((log(liczba, podstawa)))+1)]
    i = 0
    while liczba > 0:
        tab[i] = liczba % podstawa
        liczba //= podstawa
        i += 1

    tab1 = tab[::-1]
    for j in tab1:
        print(hex[j], end='')

zad1()


