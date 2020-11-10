# rok//2 = int(rok/2)
suma = 0
rok = int(input("Podaj rok "))
for a in range(1,rok//2):
    for b in range(a-1,rok//2):
        x = a
        y = b
        while y<rok:
            x, y = y, x+y
        if y==rok:
            if a+b<suma or suma==0:
                suma=a+b
                z = a,b
print(z)