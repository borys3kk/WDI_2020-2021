def zad4(tab):
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
            temp = col_sum[j] / row_sum[i]
            if temp > iloraz_max:
                iloraz_max = temp
                odp = (i, j)
    return odp, iloraz_max


if __name__ == '__main__':
    T = [[10, 7, 9],
         [5, 6, 1],
         [10, 2, 1]]
    # print(T[0][2])
    print(zad4(T))

