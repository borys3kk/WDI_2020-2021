
def zad18(A=125):
    n = 3
    a = 1
    b = 123
    e = 0.0000000001
    while abs(b-a) >= e:
        b,a = (1/n)*((n-1)*a+(A/(a**(n-1)))),b
    return a,b
print(zad18())
'''
#print(silnia(2))
def cw18(A=125.0):
    # hard to tell jak to zrobic
    n = 3
    a = 1
    b = 123
    e = 0.00000000001
    while abs(b-a) >= e:
        b,a= (1/n)*((n-1)*a+(A/(a**(n-1)))),b
    return a,b
print(cw18())
'''