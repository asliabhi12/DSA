def subArraySum(arr, n, s): 


    for k in range(n):
        sum = arr[k]

        j = k + 1

        while(j<=n):
            if sum == s:
                return [k, j-1]

            if sum > s or j == n:
                break

            sum = sum + arr[j]
            j += 1

    return 0

array = [1,2,3,7,5]

print(subArraySum(array, 5, 12))


    

   
               

print(subArraySum([1,2,3,7,5], 5, 12))
