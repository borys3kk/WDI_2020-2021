def zad5():
    t = [0 for _ in range(100)]
    k = 0
    print("Min 10 liczb zakonczonych zerem podaj byq")
    while True:
        temp = int(input('>> '))
        t[k] = temp
        if temp == 0:
            break
        k += 1
    t.sort(reverse=True)
    print(t[9])


if __name__ == '__main__':
    zad5()