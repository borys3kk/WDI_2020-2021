'''
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba zakończona jest unikalną cyfrą.
'''

def zad13():
    number = int(input('>> '))
    unikalna_cyfra = number%10
    #print(number)
    while number != 0:
        number //= 10
        cyfra = number%10
        if cyfra == unikalna_cyfra:
            return False
    return True

if __name__ == '__main__':
    print(zad13())