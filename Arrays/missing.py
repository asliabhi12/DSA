def missingNumber(arr,n):
        #Your code here
        i = 1
        while i <= n:
            if i in arr:
                if i+1 not in arr:
                    return i+1
                else: i+=1
            
            else:
                return i

arr = [8,2,3,5]

n = len(arr)

print(missingNumber(arr, n))
