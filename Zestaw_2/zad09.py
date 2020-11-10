#Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
#do k, metodą prostokątów


def funkcja_pola(x):

    print('x:',x , '1/x: ', 1/x)
    return 1/x

def zad9():
    k = float(input('Podaj przedział: '))
    n = int(input('Na ile prostokątów chcesz podzielić wykres: '))
    x = (k-1)/n
    center = 1 + ((k-1)/(2*n))
    suma = 0
    i=0


    while i < k+1:
        suma += funkcja_pola(center)
        center += x
        print(center)
        i+=1
    print(suma * x)



if __name__ == '__main__':
    zad9()
#Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale od 1
#do k, metodą prostokątów


def funkcja_pola(x):

    print('x:',x , '1/x: ', 1/x)
    return 1/x

def zad9():
    k = float(input('Podaj przedział: '))
    n = int(input('Na ile prostokątów chcesz podzielić wykres: '))
    x = (k-1)/n
    center = 1 + ((k-1)/(2*n))
    suma = 0
    i=0


    while i < k+1:
        suma += funkcja_pola(center)
        center += x
        print(center)
        i+=1
    print(suma * x)



if __name__ == '__main__':
    zad9()
