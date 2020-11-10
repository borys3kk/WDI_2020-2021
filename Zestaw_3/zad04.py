silnia = 1
n = int(input('>> '))
i = 0
to_add = 0
result = 0

while True:
    to_add = 1/silnia
    if to_add == 0:
        break
    print(to_add)
    result += to_add
    i += 1
    silnia *= i

print(result)