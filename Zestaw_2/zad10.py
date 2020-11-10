def zad10():
    number = int(input('>> '))
    a_n = 2
    a_n1 = 3*a_n +1
    while a_n <= number:
        mnoznik = 1
        while a_n*mnoznik < number:
            mnoznik += 1

        if a_n*mnoznik == number:
            return True
        a_n, a_n1 = a_n1, (3*a_n)+1
    return False

if __name__ == '__main__':
    print(zad8())