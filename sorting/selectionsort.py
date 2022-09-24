def selectionsort(arr):
    def swap(arr, a, b):
        temp = a
        a = b
        b = temp
        return a, b

    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j   
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr

arr = [8,4,6,2,1,9,0]

print(selectionsort(arr))


"""
select the smallest element and start making the list more an more sorted
from left to right

"""
