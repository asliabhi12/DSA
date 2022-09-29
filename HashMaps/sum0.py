def maxLen(arr, n):

    mydict = {}

    cursum = 0
    
    maxlen = 0

    for i in range(n):

        cursum += arr[i]

        if arr[i] == 0 and maxlen == 0:
            maxlen = 1

        if cursum == 0:
            maxlen += 1

        if cursum in mydict:
            maxlen = max(maxlen, i - mydict[cursum])

        else:
            mydict[cursum] = i

    return maxlen

arr = [15, -2, 2, -8, 1, 7, 10, 13]

print(maxLen(arr, len(arr)))
