'''
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta zawiera cyfrę równą liczbie swoich cyfr.
'''
def zad12():
    num = int(input('>> '))
    length = 0

    number = num
    while number != 0:
        length += 1
        number //= 10
    #print(num,number,length)
    while num != 0:
        cyfra = num%10
        num //= 10
        if cyfra == length:
            return True
    return False



if __name__ == '__main__':
    print(zad12())