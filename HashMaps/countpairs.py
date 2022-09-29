def getPairsCount(arr, n, k):
        # code here
        mydict = {}
        count = 0 
        for i in range(n):
            if k - arr[i] in mydict:
                count += mydict[k - arr[i]]
            mydict[arr[i]] = 1 + mydict.get(arr[i], 0)
            
        
        return count

        # print(mydict)
        # sum = 0    
        # for k in mydict.values():
        #     sum += k

        # print(sum)
        # for i in mydict:
        #     print(i)
        
        
        # counter = 0
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if i != j and arr[i] + arr[j] == k:
        #            counter += 1

        # return counter  

arr = [1, 1, 1, 1]
n = len(arr)
k = 2

print(getPairsCount(arr, n, k))