def zad7():
    searched_number = int(input('>> '))

    n = 1
    a_n = n*n + n + 1

    while a_n < searched_number:
        mnoznik = 2
        while a_n * mnoznik < searched_number:
            mnoznik += 1
        if a_n * mnoznik == searched_number:
            print("true")
            return 1
        n += 1
        a_n = n*n + n + 1
    return False


if __name__ == '__main__':
    zad7()
