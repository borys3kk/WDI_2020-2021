'''
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
'''
def zad7():
    liczba_szukana = int(input("Podaj liczbe: "))
    a1 = 1
    a2 = 1
    while True:
        if liczba_szukana == a1*a2:
            return True
        elif a1*a2 > liczba_szukana:
            return False
        else:
            a1, a2 = a1+a2, a1


print(zad7())