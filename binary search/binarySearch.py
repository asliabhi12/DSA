def binarysearch(arr, n, k):
        l = 0
        r = n - 1
        
        while l <= r:
                mid = (l+r)//2
                print("mid is ",arr[mid])

                if arr[mid] == k:
                    print("mid is ",mid)
                    return mid
            
                elif arr[mid] > k:
                    r = mid -1
                    print("right is ",arr[r])

                else:
                    l = mid + 1
                    print("left is", arr[l])
        print("not found")

arr = [1,2,3,4,5,6,7]

print(binarysearch(arr, len(arr), 7))