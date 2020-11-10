def zad15():
    e = 0.00000000000001
    return_value = (0.5)**(0.5)
    value_of_return_before = 2
    value_before = (0.5)**(0.5)

    while abs(value_of_return_before-return_value)>=e:
        temp = ((0.5)+((.5)*value_before))**(.5)
        value_of_return_before = return_value
        return_value *= temp
        value_before = temp
    return 2.0/return_value
print(zad15())