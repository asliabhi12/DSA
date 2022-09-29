
def equilibriumPoint(A, N):
    t = sum(A)
    l = 0
    for i in range(N):
        t -= A[i]
        if l == t:
            return i+1
        else:
            l += A[i]
    return -1
        

        
    
    
    
    
    
    
    
    
    
    # r = {}
    # l = {}

    # def findleftSum(i):
    #     lsum = 0
    #     for j in range(0,i):
    #         lsum += A[j]
    #     return lsum

    # def findrightSum(i):
    #     rsum = 0
    #     for j in range(i+1, N):
    #         rsum += A[j]

    #     return rsum


    # for i in range(N):
    #     lsum = findleftSum(i)
    #     rsum = findrightSum(i)
    #     l[i] = lsum
    #     r[i] = rsum
    
    # print(l[2])
    # print(r[2])


    # for i in range(N):
    #     if l[i] == r[i]:
    #         return i + 1
    # return -1
        

arr= [1,3,5,2,2]

print(equilibriumPoint(arr, len(arr)))