def missingNumber(arr,n):
        #Your code here
        for i in range(n):
            if arr[i] < 0:
                arr[i] = 0
        
        print(arr)
                
        for i in range(n):
            val = abs(arr[i])
            if 1 <= val <= n:
                if arr[val-1] > 0:
                    arr[val-1] *= -1
                if arr[val-1] == 0:
                    arr[val - 1] = -1 * (n + 1)
        
        print(arr)
                    
        for i in range(1,n+1):
            if arr[i-1] >= 0:
                return i 
                
        return (n + 1)

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(missingNumber(arr, len(arr)))