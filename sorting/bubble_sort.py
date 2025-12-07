a = [2,10,19,455,321,999,3,1]
res = []
print(len(a))
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i]>a[j]):
            res[i] = a[i]

print(res)