'''
def zad4(N):
    liczba = 1
    while liczba <= N:
        if liczba%2==0 and liczba%3==0 and liczba%4==0:
            while liczba%2==0:
                liczba
'''
def zad4(N : int):
    count = 0
    while N >= 1:
        a = N
        while a % 2 == 0:
            a //= 2
        while a % 3 == 0:
            a //= 3
        while a % 5 == 0:
            a //= 5
        if a == 1:
            count += 1 
        N -= 1
    return count 

if __name__ == "__main__":
    print(zad4(1000000))