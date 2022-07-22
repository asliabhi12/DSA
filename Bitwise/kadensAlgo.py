def maxSumSubArray(Arr):
    max_sum = 0
    curr_sum = 0
    for i in range(len(Arr)):
        curr_sum += Arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum

print(maxSumSubArray([3,5,-4,3,-2]))