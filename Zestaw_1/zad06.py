#Proszę napisać program rozwiązujący równanie x^x = 2020 metodą bisekcji
'''
def f(x):
    return x**x - 2020
def zad6():
    a = 0
    b = 10
    e = 0.0000000000001
    while True:
        x1 = ((a+b)/2)
        if b-a <= e:
            break
        elif f(a)*f(x1) < 0:
            b = x1
        else:
            a = x1
            #print(f"to jest a {a}")
    return(x1)

print(zad6())
'''
acc = 0.00001
a = 0
b = 10
while(b-a) > acc:
    x=(a+b)/2
    if(x**x > 2020):
        b=x
    else:
        a=x
print(x)

#print(zad6()**zad6()
#print(0**0)
