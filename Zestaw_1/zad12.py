def nwd(a,b):
    while True:
        if a>b:
            a-=b
        elif a<b:
            b-=a
        elif a==b:
            return a

def zad12(a,b,c):
    x = nwd(a,b)
    y = nwd(x,c)
    return(nwd(x,y))


print(zad12(300,30,3000))
#print(nwd(6,105))