from math import sqrt
def zad10(liczba):
    maximum = 10**6

def zad8(liczba):
    n=1
    if liczba == 2:
        return True
    elif liczba % 2 ==0:
        return False
    else:
        while n < int(sqrt(liczba)):
            n+=2
            #print(n)
            if liczba%n==0:
                return False
            
    return True
liczba = 2**x - 1 
if zad8(liczba):
