def findMin(nums) -> int:
        l, res = 0, nums[0]
        r = len(nums) -1
        while (l <= r):
            if nums[l] < nums[r]:
                res = min(res,nums[l])
                break
            half = (l + r) // 2
            res = min(res, nums[half])
            if nums[half] >= nums[l]:
                l = half + 1
            else:
                r = half-1
                
            
        return res


print(findMin([4,5,6,7,0,1,2]))