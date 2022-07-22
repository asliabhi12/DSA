from itertools import count
from tabnanny import check


def majorityElement(arr):
    ansIndex = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == arr[ansIndex]:
            count += 1
        else:
            count -= 1
        if count == 0:
            ansIndex = i
            count = 1
       # no majority element       
    return arr[ansIndex]

print(majorityElement([3,5,-4,3,3, -2, 2,2 ]))


