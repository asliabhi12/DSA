n1, k=map(int,input().split()) 
l1=list(map(int, input().split()))

l2=[]

for i in range(k):

    index1, index2=map (int, input().split())
    l1[index1-1]=index2
    count=1
    t=l1[0]

    for j in range(1, n1):
        if t!=l1[j]:
            count+=1

        t=l1[j]

    l2.append(count)

print(*l2)