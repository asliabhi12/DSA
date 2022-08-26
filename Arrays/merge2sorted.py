def merge(nums1, m: int, nums2, n: int) -> None:
        nums1_copy = nums1[:m]
        i = 0
        j = 0

        while(i < m and j < n):
            if nums1_copy[i] < nums2[j]:
                nums1[i+j] = nums1_copy[i]
                i += 1
            else: 
                nums1[i+j] = nums2[j]
                j +=1


        if i == m:
            for k in range(j,n):
                nums1[m+k] = nums2[k]
        else:
            for k in range(i,m):
                nums1[n+k] = nums1_copy[k]
        


        nums1_copy = nums1[:m]
        i,j = 0, 0 
        
        while i < m and j < n:
            if nums1_copy[i] > nums2[j]:
                nums1[i+j] = nums2[j]
                j += 1
            else:
                nums1[i+j] = nums1_copy[i]
                i += 1
        
        if i == m:
            for k in range(j,n):
                nums1[m+k] = nums2[k]

        else:
            for k in range(i,m):
                nums1[n+k] = nums1_copy[k]