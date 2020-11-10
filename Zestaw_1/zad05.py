#Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
def zad5(A):
    a = A/2
    e = 0.00000000001
    while abs(A/a - a) >= e:

        a = (A/a + a)/2
        
    return a


print(zad5(int(input("Podaj liczbe: "))))
