from random import randint
from time import sleep

def zad2(T):
    num = 0
    for col in range(len(T)):
        is_in_row = False
        for row in range(len(T[col])):
            # print(T[col][row], end=' ')
            is_even = True
            copy = T[col][row]
            while copy > 0:
                if (copy % 10) % 2 == 0:
                    is_even = False
                    break
                copy //= 10
            if is_even:
                is_in_row = True
                break
        if not is_in_row:
            return False
    return True


if __name__ == '__main__':
    # N = 7
    # T = [[randint(1,1000) for col in range(N)]for row in range(N)]
    T = [[893, 248, 966, 910, 531, 871, 8],
         [677, 630, 266, 125, 902, 331, 893],
         [969, 303, 323, 642, 475, 599, 708],
         [211, 229, 772, 920, 969, 351, 940],
         [942, 322, 896, 79, 259, 28, 692],
         [836, 958, 199, 666, 881, 249, 935],
         [347, 71, 420, 831, 735, 169, 75]]
    print(zad2(T))
