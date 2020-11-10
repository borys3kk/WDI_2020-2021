def zad10():
    maximum = 10**6
    for a in range(4,maximum+1):
        suma = 0
        for i in range(a-1,0,-1):            
            if a % i == 0:
                suma += i
        if suma == a:
            print("Liczba doskonała: ",a)
zad10()