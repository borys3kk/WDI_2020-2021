from random import randint

def zad6():
    #N = 100
    #t = [0]*N
    t = [49, 731, 805, 52, 182, 121, 270, 166, 412, 720]
    for i in range(len(t)):
        count = 0
        #t[i] = randint(1,1000+1)
        copy = t[i]
        while copy != 0:
            if (copy % 10) % 2 == 1:
                count += 1
                break
            copy //= 10
        if count == 0:
            return False
    return True
    #print(t)


if __name__ == '__main__':
    print(zad6())
