#Napisać program wypisujący podzielniki liczby.
def zad9(liczba):
    factors=[]
    i=0
    while i<liczba:
        i+=1
        if liczba%i==0:
            factors.append(i)
    return factors
factors = zad9(int(input("Podaj liczbe: ")))

for i in factors:
    print(i)

