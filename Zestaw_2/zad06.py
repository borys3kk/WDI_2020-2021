def zad6():
    liczba = int(input("Podaj liczbę: "))
    factors=[]
    i=0
    a = int(liczba**(0.5))
    if a*a == liczba:
        b = a
        return a, b
    while i < liczba:
        i+=1
        if liczba%i==0:
            factors.append(i)
    a = factors[len(factors)//2-1]
    b = factors[len(factors)//2]
    if a*b == liczba:
        return a,b
    else:
        print("Sposób nie działa")
        return False
print(zad6())

