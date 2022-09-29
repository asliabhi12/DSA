from msilib import PID_TITLE


def inversionCount(arr, n):
        # Your Code Here
        count = 0
        
        for i in range(n):
            for j in range(i, n):
                if arr[i] > arr[j] and i < j:
                    count += 1
        
        return count

ar = [2, 3, 4, 5, 6]
print(inversionCount(ar, len(ar)))