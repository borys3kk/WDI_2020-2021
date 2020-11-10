def fibonnacci():
    f1, f2 = 1, 1
    print(f1)
    print(f2)
    while True:
        f1, f2 = f1+f2, f1
        if f1 > 1000000:
            break
        else:
            print(f1)

if __name__ == '__main__':
    fibonnacci()
#poprawić żeby było na 2 zmienne
