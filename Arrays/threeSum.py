

def threeSum(nums):
        # res = []
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i]+ nums[j] +nums[k] ==0:
        #                 return [nums[i],nums[j],nums[k]]
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            print(i,a)

            l,r = i+1, len(nums)-1

            while l < r:
                threeSum = a + nums[l] + nums[r] 
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l +=1
                else: 
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        
        return res

print(threeSum([-1,0,1,2,-1,-4]))