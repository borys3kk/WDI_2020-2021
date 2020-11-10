from random import randint


def zad5(tab):
    row_sum = [0] * len(tab)
    col_sum = [0] * len(tab)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            col_sum[i] += tab[j][i]
            row_sum[i] += tab[i][j]
    iloraz_max = 0
    odp = (1, 1)
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if row_sum[i] == 0:
                continue
            temp = col_sum[j] / row_sum[i]
            if temp > iloraz_max:
                iloraz_max = temp
                odp = (i, j)
    return odp, iloraz_max


if __name__ == '__main__':
    N = 10
    T = [[randint(-10, 10) for _ in range (N)]for _ in range(N)]
    # print(T[0][2])
    print(zad5(T))