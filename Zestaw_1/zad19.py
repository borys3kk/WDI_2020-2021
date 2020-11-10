def silnia(liczba):
    ret = 1
    for i in range(1,liczba+1):
        ret*=i
        #print(ret)
    return ret

def zad19():
    ret = 0.0
    for i in range(0,1000):
        print(i)
        ret+= 1/silnia(i)
    return ret

print(zad19())
#print(silnia(2))