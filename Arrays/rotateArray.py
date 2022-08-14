def rotate(nums, k):
    k = k % len(nums)
    def reverse(l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l+1, r-1
                
    reverse(l=0, r=len(nums)-1)
    reverse(l=0, r=k-1)
    reverse(l=k, r=len(nums)-1)

    return nums

print(rotate([1,2,3,4,5],3))
       
        