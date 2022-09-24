def subArraySum(arr, n, s): 
       #Write your code here
    for i in range(n):
        sum = arr[i]
        for j in range(i + 1, n):
            if sum == s:
                return [i+1, j]

            if sum > s or j == n:
                break
            sum = sum + arr[j]
                
                

array = [1,2,3,4,5,6,7,8,9,10]

print(subArraySum(array, 10, 15))