#Napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina
from math import *
def zad14(x):
    x1 = 0
    x2 = 2
    n = 0
    suma = 0
    while abs(x1-x2)> 0.0000001:
        x1, x2 = x2, szereg(x,n)
        suma+=x2
        print(suma,x2)
        n+=1

def silnia(liczba):
    ret = 1
    for i in range(1,liczba+1):
        ret*=i
    return ret

def szereg(x,n):
    return ((-1)**n)*(x**(2*n))/silnia(2*n)

zad14(pi/3)



'''
def silnia(y):
    s=y
    while y>1:
        y-=1
        s*=y
    return s

wynik = 1
prev = 0
accuracy = 0.000001
i = 1
x = pi/6
while abs(prev-wynik) > accuracy:
    prev = wynik
    if i % 2 == 0:
        wynik += (1/silnia(i*2)) * pow(x, i*2)
    else:
        wynik -= (1/silnia(i*2)) * pow(x, i*2)
    i += 1

print(wynik)
'''
