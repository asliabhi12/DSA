a = [2,1,3,4,5,6,8]

a.sort()

for i in range(len(a)+1):
    if a[i+1] != a[i] + 1:
        print(a[i]+1)


print(a)