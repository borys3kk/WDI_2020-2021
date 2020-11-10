from math import sqrt
def zad8(liczba):
    n=3
    if liczba == 2 or liczba == 3: return True
    elif liczba == 1 or liczba % 2 == 0 or liczba % 3 == 0: return False
    else:
        while n < int(sqrt(liczba)):
            n+=2
            #print(n)
            if n%3==0:
                pass
            elif liczba%n==0: return False
            
    return True
    
print(zad8(int(input("Podaj liczbe: "))))