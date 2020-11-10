from random import randint


def zad7():
    '''
    N = 100
    t = [0]*N
    '''
    t = [529, 7312, 925, 521, 1932, 1231, 3721, 1325, 3129, 712]
    even_count = 0
    for i in range(len(t)):
        # t[i] = randint(1,1000+1)
        copy = t[i]
        while copy != 0:
            if (copy % 10) % 2 == 0:
                even_count += 1
                break
            copy //= 10
    if even_count == len(t):
        return False
    else:
        return True


if __name__ == '__main__':
    print(zad7())
