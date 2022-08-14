
def searchInfinite(arr, key):
    def binarySearch(arr, l, r, x):
 
    # Check base case
        if r >= l:
 
            mid = l + (r - l) // 2
 
        # If element is present at the middle itself
            if arr[mid] == x:
                return mid
 
        # If element is smaller than mid, then it
        # can only be present in left subarray
            elif arr[mid] > x:
                return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present
        # in right subarray
            else:
                return binarySearch(arr, mid + 1, r, x)
 
        else:
        # Element is not present in the array
            return -1
    
    low = 0
    high = 2
    while(arr[high] < key):
        low = high
        high = high * 2
    return binarySearch(arr, low, high, key)



print(searchInfinite([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170], 100))