"""
Dwie liczby naturalne są różno-cyfrowe jeżeli nie posiadają żadnej wspólnej cyfry.
 Proszę napisać program, który wczytuje dwie liczby naturalne i poszukuje najmniejszej podstawy systemu (w zakresie
2-16) w którym liczby są różno-cyfrowe. Program powinien wypisać znalezioną podstawę, jeżeli podstawa
taka nie istnieje należy wypisać komunikat o jej braku. Na przykład: dla liczb 123 i 522 odpowiedzią jest
podstawa 11 bo 123(10) = 102(11) i 522(10) = 435(11).
"""

# zakładam że liczby są takiej samej długośći
# edit w sumie nie musze xD
from math import log


def zmianaPodstawy(liczba, podstawa):
    hex_str = "0123456789ABCDEF"
    tab = [0 for _ in range(int((log(liczba, podstawa))) + 1)]
    i = 0
    while liczba > 0:
        tab[i] = liczba % podstawa
        liczba //= podstawa
        i += 1
    tab1 = tab[::-1]
    i = 0
    for j in tab:
        # noinspection PyTypeChecker
        tab1[i] = hex_str[j]
        # print(hex[j])
        i += 1
    return tab1


def zad20():
    liczba1 = int(input('>> '))
    liczba2 = int(input('>> '))
    # liczba1 = 1232
    # liczba2 = 4254

    while True:
        for i in range(3, 16 + 1):
            counter = 0
            zmiana1 = zmianaPodstawy(liczba1, i)
            zmiana2 = zmianaPodstawy(liczba2, i)
            for j in range(len(zmiana1)):
                if zmiana1[j] not in zmiana2:
                    counter += 1
                if counter == len(zmiana1):
                    return i
        return False


if __name__ == '__main__':
    print(zad20())
