def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                swapped = True

        if swapped == False:
            break

    return arr

print(bubbleSort([9,5,4,3]))

