def rekurencja(a_n):
    return (a_n%2)*(3*a_n+1)+(1-a_n%2)*(a_n/2)
def zad16():
    maksimum = 0
    liczba = 0
    for i in range (2,10000+1):
        count = 0
        a_n = i
        while abs(a_n-1) > 0.000000054:
            a_n = rekurencja(a_n)
            count += 1
        if count > maksimum:
            maksimum = count
            liczba = i
    return maksimum , liczba

print(zad16())