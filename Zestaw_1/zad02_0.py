f0=0
f1=0
tmp=0
i,j=1,1
result_i = 0
result_j = 0
target = int(input("Podaj rok: "))
best = target

while i<int(target/2):
    while j<int(target/2):
        i+=1
        f0=i
        f1=j
        while f0+f1<target+2:
            tmp = f0+f1
            if tmp==target:
                if i+j<best:
                    result_i = i
                    result_j = j
                    best = i+j
            f0 = f1
            f1 = tmp 
            print(tmp,i,j)
        j+=1
print(result_i,result_j)
