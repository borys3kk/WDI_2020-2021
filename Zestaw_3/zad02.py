def zad2():
    a = input('>> ')
    b = input('>> ')
    if len(a) != len(b):
        return False
    taba = [0]*len(a)
    tabb = [0]*len(b)
    for i in range(len(a)):
        taba[i] = a[i]
        tabb[i] = b[i]
    taba.sort()
    tabb.sort()
    for i in range(len(a)):
        if taba[i] != tabb[i]:
            return False
    return True


if __name__ == '__main__':
    print(zad2())
