def trappingWater(arr,n):
        #Code here
        
        #preprocessing
        left = [0]*n
        maxi = arr[0]
        for i in range(n):
            maxi = max(maxi, arr[i])
            left[i] = maxi
        print(left)


        right = [0]*n
       
        
        
        maxi = arr[n-1]
        for i in range(n-1,-1,-1):
            maxi = max(maxi, arr[i])
            right[i] = maxi
        print(right)
        new = []
        res = 0
        for i in range(n):
            res =  res + (min(left[i], right[i]) - arr[i])
            

        return res
            

     


arr = [1, 1, 5, 2, 7, 6, 1, 4, 2, 3]
print(trappingWater(arr, len(arr)))

