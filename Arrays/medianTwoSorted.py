def findMedianSortedArrays(nums1, nums2) -> float:

        a,b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        # set a as the shorter list 
        
        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) -1
        
        while True:
            i = (l+r) // 2 # a pointer
            j = half - i - 2 # b pointer
            
            Aleft = a[i] if i >= 0 else float('-infinity')
            Aright = a[i+1] if (i + 1) < len(a) else float('infinity')
            Bleft = b[j] if j >= 0 else float('-infinity')
            Bright = b[j+1] if (j + 1) < len(b) else float('infinity')

            
            
            
            if Aleft <= Bright and Bleft <= Aright:
                
                if total % 2:
                    return min(Bright, Aright)  
                return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else: 
                l = i + 1

a = [1,2,3]
b = [4,5,6]

print(findMedianSortedArrays(a,b))