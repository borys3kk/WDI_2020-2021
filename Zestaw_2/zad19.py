'''
Napisać program wczytujący dwie liczby naturalne a,b i wypisujący rozwinięcie dziesiętne
ułamka a/b w postaci ułamka okresowego. Na przykład 1/3 = 0.(3), 1/6 = 0.1(6), 1/7 = 0.(142857)
'''

def ex19():

    a, b = 1, 7
    first_a = -1
    spaces = max(factorize(b, 2), factorize(b, 5))
    print(a//b, end='.')

    a %= b
    while True:
        cnt = 0
        while a < b:
            a *= 10
            cnt += 1

        if cnt > 1:
            print(0, end='')

        if a == first_a:
            break

        if spaces == 0:
            print('(', end='')
            first_a = a

        print(a//b, end='')
        a %= b
        spaces -= 1

    print(')')

def factorize(n, factor):
    cnt = 0
    while n % factor == 0:
        n //= factor
        cnt += 1
    return cnt
print(ex19())