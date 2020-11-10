
def zad3(T):

    for col in range(len(T)):
        licznik = 0
        for row in range(len(T[col])):
            # print(T[col][row], end=' ')
            copy = T[col][row]
            while copy > 0:
                if (copy % 10) % 2 == 0:
                    licznik += 1
                    break
                copy //= 10
        if licznik == len(T[col]):
            return True
    return False


if __name__ == '__main__':
    T = [[993, 537, 999],
         [597, 579, 359],
         [972, 312, 351]]
    print(zad3(T))
