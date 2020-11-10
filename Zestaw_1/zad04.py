x = int(input())
suma = 0
odd = 1
n = 0
while suma <= x:
    suma += odd
    odd += 2
    n += 1
print(n-1)

