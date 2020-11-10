
def search(x, mask=1):
    right = x % mask
    left = x // (mask * 10)
    left *= mask
    new_x = left + right
    result = 0

    if new_x%7 == 0 and new_x != 0:
        result += 1
    print(left, right, new_x)
    if mask < new_x:
        result += search(new_x, mask)
    if mask * 10 < x:
        result += search(x, mask * 10)
    return result


if __name__ == '__main__':
    #x = int(input('Podaj liczbe: '))
    print(search(2315))
    #search(2315,1)
    #print(2315%1)
#print(2315//10)
