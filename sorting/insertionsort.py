def insertionsort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j + 1] = temp
    
    return arr

arr = [8, 4,6,2,1,9,0]

print(insertionsort(arr))

"""
we start i from 1 and compare previous element with i and swap it position,
this process continues until we don't find an element which is 
smaller and smallest element is swaped with temp
"""
