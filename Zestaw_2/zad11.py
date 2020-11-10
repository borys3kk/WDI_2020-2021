'''
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
jej cyfry stanowią ciąg rosnący.
'''
def zad11():
    num = int(input('>> '))

    a = 10

    while num != 0:
        temp = num%10
        num //= 10
        if temp >= a:
            return False
        a = temp
    return True

if __name__ == '__main__':
    print(zad11())