L = [1,2,3,4,5,6,7,8,9,10]
L1 = []
for i in range(len(L)):
    if i % 3 == 0:
        L1.append(L[i])
print(L1)
