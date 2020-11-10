from math import sqrt
licznik = 0
N = int(input('>> '))

tab = [True for _ in range(N+1)]
tab[0] = tab[1] = False

#i = 2
for i in range(2, int(sqrt(N))+1):
    if tab[i]:
        for a in range(i*i,N+1,i):
            #print(a)
            tab[a] = False

print('')
for i in range(N+1):
    if tab[i]:
        #print(i)
        licznik += 1
print(licznik)

#[print(i) for i in range(10)]