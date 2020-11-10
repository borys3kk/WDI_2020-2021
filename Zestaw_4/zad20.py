"""
Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi
"""
# from random import randint
N = 5
# T = [[randint(1, 100) for _ in range(N)] for _ in range(N)]
T = [[6, 94, 53, 33, 11],
     [52, 74, 7, 19, 49],
     [59, 77, 78, 79, 80],
     [24, 75, 67, 24, 55],
     [100, 51, 42, 9, 17]]


# T[wiersz](-)[kolumna](|)
# sumy[0][0] = 197 + 241 - 6 = 432


def zad20(tab):
    dl = len(tab)
    sumy = [[0 for _ in range(dl)] for _ in range(dl)]
    # sumyKolumn = [[0 for _ in range(dl)] for _ in range(dl)]
    # print(tab[1][0])

    for row in range(dl):
        suma = 0
        for col in range(dl):
            sumy[row][col] = sum(tab[row]) - tab[row][col]
            suma += tab[col][row]
        # print(suma)
        for i in range(dl):
            sumy[i][row] += suma
        # sumy[col][row] += suma

        # print(suma)
        # sumy[row][col] += suma
    # print(sumy)
    tmp1 = 0
    tmp2 = 0
    w1 = 0, 0
    w2 = 0, 0
    for m in range(dl):
        for n in range(dl):
            # print(m, n)
            if sumy[m][n] > tmp1 or sumy[m][n] > tmp2:
                tmp2 = tmp1
                tmp1 = sumy[m][n]
                w2 = w1
                w1 = (m, n)
    return w1, w2

    # print(sumyKolumn)


"""
for i in range(dl):
    suma = 0
    for j in range(dl):
        suma += T[i][j]
    sumyWierszy[j][i] = suma
"""

if __name__ == '__main__':
    print(zad20(T))
