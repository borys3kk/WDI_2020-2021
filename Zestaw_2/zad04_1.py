end = None
def zad4_1():
    n = int(input(">>"))
    l = 0

    a2 = 1
    while a2 <= n:
        a3 = a2
        while a3 <= n:
            a5 = a3
            while a5  <= n:
               l +=1
               a5 *= 6
            end
            a3 *= 3
        end
        a2 *= 2
    print(l)
zad4_1()