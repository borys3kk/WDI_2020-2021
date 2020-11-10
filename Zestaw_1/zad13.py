def nwd(a,b):
    while True:
        if a>b:
            a-=b
        elif a<b:
            b-=a
        elif a==b:
            return a

def zad13(a,b,c):
    nww_a_b = a*b/nwd(a,b)
    nww_a_b_c = nww_a_b*c/nwd(nww_a_b,c)
    if nww_a_b == nww_a_b_c:
        return int(nww_a_b)
print(zad13(24,3,6))