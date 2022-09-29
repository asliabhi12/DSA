def maxLen(arr, n):
        #Code here
        maxlen = 1
        for i in range(n):
            sum = arr[i]
            for j in range(i+1, n):
                sum += arr[j]
                if sum == 0:
                    maxlen = max(len(arr[i:j+1]), maxlen)

        return maxlen

arr = [0]

print(maxLen(arr, len(arr)))