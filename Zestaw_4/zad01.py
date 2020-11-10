"""
Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali. """
from time import sleep
from os import system
from random import randint


def wypisz_tab(tablica):
    print('')
    for col in range(len(tablica)):
        for row in range(len(tablica[col])):
            if (tablica[col][row]) < 10:
                print(' ', tablica[col][row], sep='', end=' ')
            else:
                print(tablica[col][row], end=' ')
        print('')


def zad1(T):
    # T[0][9] = 1
    num = 1
    l = 0
    p = N
    g = 0
    d = N
    while num <= N ** 2:
        for i in range(l, p):
            T[g][i] = num
            # print(T[g][i], end=' ')
            num += 1
        g += 1
        for j in range(g, d - 1):
            T[j][p - 1] = num
            # print(T[j][p - 1], end=' ')
            num += 1
        p -= 1
        for k in range(p, l, -1):
            T[d - 1][k] = num
            # print(T[d - 1][k], end=' ')
            num += 1
        d -= 1
        for m in range(d, g - 1, -1):
            T[m][l] = num
            # print(T[m][l], end=' ')
            num += 1
        l += 1
    return T


if __name__ == '__main__':
    N = 9
    T = [[randint(1, 100) for col in range(N)] for row in range(N)]
    wypisz_tab(zad1(T))
