def maxElement(arr, k):
    list = []
    for i in range(0, len(arr)-k):
        max = arr[i]
        for j in range(1,k):
            if arr[i+j] > max:
                max = arr[i+j]
        list.append(max)
    return list

print(maxElement([1,2,3,4,3,2,5,9], 3))