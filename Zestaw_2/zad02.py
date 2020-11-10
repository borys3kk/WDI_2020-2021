def zad2(a,b,n=100):
    print(a//b, end="")
    a = a%b
    print(",",end="")
    while n >0:
        if a < b:
            a *= 10
            print(a//b, end="")
            a = a%b
        else:
            print(a//b,end="")
            a = a%b
        n-= 1
zad2(6,70000)
a = 6
b = 7000
a = a%b
#print(a)