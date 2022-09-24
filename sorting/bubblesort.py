
def bubblesort(arr):
    def swap(arr, a, b):
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp
    
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j+1] < arr[j]:
                swap(arr, j+1, j)
                #arr[j+1], arr[j] = arr[j], arr[j+1]
        
    return arr



"""
In this we swap array elements one by one n-i-1 times for each iteration
"""

arr = [1,2,3,5,6,8,4, 10, 19, 78,5,54]

print(bubblesort(arr))

    
