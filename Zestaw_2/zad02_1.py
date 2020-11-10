def zad3_1():
    licznik = int(input())
    mianownik = int(input())
    n = int(input())
    c = licznik // mianownik
    print(c, end='.')
    r = (licznik % mianownik)

    for i in range(n):
        r = 10 * r
        print(r // mianownik, end='')
        r = r % mianownik


zad3_1()
