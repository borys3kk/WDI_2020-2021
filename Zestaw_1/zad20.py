def zad20():
    a_n = 20.0
    b_n = 30.0
    a_n, b_n = (a_n*b_n)**(0.5), (a_n+b_n)/2
    while abs(a_n - b_n) > 0.0000000000001:
        a_n, b_n = (a_n*b_n)**(0.5), (a_n+b_n)/2
    return b_n
print(zad20())