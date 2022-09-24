def getMinDiff(arr, n, k):
        # code here
        mid =  arr[0] + (arr[n-1] - arr[0]) // 2
        
        for i in range(n):
            if arr[i] <= k:
                arr[i] += k

            
            elif arr[i] <= mid:
                arr[i] += k 
            elif arr[i] > mid:
                arr[i] -= k

        dif = max(arr) - min(arr)
        
        return dif

arr = [2, 6, 3, 4, 7, 2, 10, 3, 2, 1]

print(getMinDiff(arr, len(arr), 5))

