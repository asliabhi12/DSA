def duplicates(arr, n): 
        # code here
        arr2 = []
        arr3 = []
        for k in range(n):
                if arr[k] not in arr2:
                    arr2.append(arr[k])
                else:
                    arr3.append(arr[k])
        arr3.sort()            
        if arr3:
            return [*set(arr3)]
        else:
            return [-1]


arr= [2,3,1,2,3,2]


print(duplicates(arr, len(arr)))